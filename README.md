# multi-gpu-torch-profile-view
merge and view torch profile json result in cluster training

# usage
```bash
python profile_merge.py ./*.json -o merge.json # merge multirank profile
# use perfetto to view large trace
url -LO https://get.perfetto.dev/trace_processor
chmod +x ./trace_processor
trace_processor --httpd merge.json
```