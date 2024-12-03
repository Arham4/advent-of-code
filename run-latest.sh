latest_dir=$(ls -td -- 20*/ | head -n 1)
echo Running latest from $latest_dir
cd ./$latest_dir && chmod +x ./run-latest.sh && ./run-latest.sh