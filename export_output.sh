#!/usr/bin/env bash

rm ../1_2000/*.png
rm ../2001_4000/*.png
rm ../3000_4000/*.png
rm ../4001_5000/*.png
rm ../5001_N/*.png

mv output/{00001..02000}.png ../1_2000/
mv output/{02001..04000}.png ../2001_4000/
mv output/{04001..05000}.png ../4001_5000/
mv output/{05001..09000}.png ../5001_N/

