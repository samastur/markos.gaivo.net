#!/bin/sh
# Deploy root/ (the homepage and its assets) to markos.gaivo.net.
#
# Rebuilds root/index.html from homepage/about.md, then rsyncs root/ to the
# web root. The blog lives in articles/ on the server and is deployed by
# articles/Makefile; it is excluded here and never touched.
#
# Nothing is deleted on the server unless you pass --delete, and even then
# articles/ stays protected.
#
# Usage:
#   ./deploy_root.sh            # build and upload
#   ./deploy_root.sh -n         # dry run: show what would change
#   ./deploy_root.sh --delete   # also remove remote files missing locally
#
# Override the target with env vars, e.g. SSH_TARGET_DIR=/tmp/x ./deploy_root.sh
set -eu

SSH_HOST=${SSH_HOST:-vimes.neko.si}
SSH_PORT=${SSH_PORT:-22}
SSH_USER=${SSH_USER:-markos}
SSH_TARGET_DIR=${SSH_TARGET_DIR:-/home/markos/gaivo}

cd "$(dirname "$0")"

./build_homepage.py

# The repo keeps the Apache config unhidden as htaccess; it goes live as
# .htaccess. Excluded files (articles/, editor junk) are never deleted remotely.
rsync -e "ssh -p $SSH_PORT" -rvzc --itemize-changes \
    --exclude='/articles/' \
    --exclude='/htaccess' --exclude='/.htaccess' \
    --exclude='.*.swp' --exclude='.DS_Store' \
    "$@" \
    root/ "$SSH_USER@$SSH_HOST:$SSH_TARGET_DIR/"

rsync -e "ssh -p $SSH_PORT" -vzc --itemize-changes \
    $(printf '%s\n' "$@" | grep -x -e '-n' -e '--dry-run' || true) \
    root/htaccess "$SSH_USER@$SSH_HOST:$SSH_TARGET_DIR/.htaccess"
