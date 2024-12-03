latest_dir=$(ls -td -- day*/ | head -n 1)
echo Running $latest_dir
cd ./$latest_dir && chmod +x ./run.sh && ./run.sh