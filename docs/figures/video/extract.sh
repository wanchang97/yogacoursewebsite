#!/bin/bash
# Idempotent extractor: run repeatedly until "ALL DONE". MODE=still|clip|all  BUDGET=seconds
OUT="$HOME/mnt/Yoga/YogaCourseWebsite/docs/figures/video"; VD="$HOME/mnt/trainingVideo"
MODE=${1:-all}; BUDGET=${2:-140}; T0=$(date +%s); n=0; skip=0
tail -n +2 "$OUT/catalog.csv" | while IFS=, read order slug zh type vid start end; do
  [ "$MODE" != all ] && [ "$MODE" != "$type" ] && continue
  V="$VD/sideview1.mp4"; [ "$vid" = 2 ] && V="$VD/sideview2.MP4"
  if [ "$type" = still ]; then f="$OUT/$slug.jpg"; else f="$OUT/clips/$slug.mp4"; fi
  [ -s "$f" ] && { skip=$((skip+1)); continue; }
  [ $(( $(date +%s) - T0 )) -ge $BUDGET ] && { echo "BUDGET_HIT after $n items (skipped $skip existing)"; exit 0; }
  if [ "$type" = still ]; then
    ffmpeg -nostdin -ss "$start" -i "$V" -frames:v 1 -vf scale=1280:-1 -q:v 2 "$f" -y -loglevel error
  else
    ffmpeg -nostdin -ss "$start" -i "$V" -t $((end-start)) -vf "scale=640:-1,fps=15" -an -c:v libx264 -preset veryfast -crf 26 -pix_fmt yuv420p -movflags +faststart "$f" -y -loglevel error
  fi
  echo "ok $order $slug ($type)"; n=$((n+1))
done
echo "ALL DONE (this run: new items processed; existing skipped)"
