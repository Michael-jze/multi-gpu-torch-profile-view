python profile_merge.py ./*.json -o merge.json
url -LO https://get.perfetto.dev/trace_processor
chmod +x ./trace_processor
trace_processor --httpd merge.json