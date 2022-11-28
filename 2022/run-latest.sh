latest_dir=$(ls -td -- day*/ | head -n 1)
cd ./$latest_dir && chmod +x ./run.sh && ./run.sh
echo RAN $latest_dir