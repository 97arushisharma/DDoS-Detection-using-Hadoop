#!/bin/bash  
sudo tshark -a duration:10 | /home/adit/hadoop/bin/hadoop fs -put - /tshark_attack
sudo /home/adit/hadoop/bin/hadoop jar /home/adit/Desktop/hadoop-streaming-2.8.3.jar -mapper /home/adit/Downloads/mapper1.py -reducer /home/adit/Downloads/reducer1.py -input /tshark_attack -output /attack_output
for i in {1..49}
    do
        sudo tshark -a duration:10 | /home/adit/hadoop/bin/hadoop fs -put -f - /tsharka1
        sudo /home/adit/hadoop/bin/hadoop fs -cat /tsharka1 | /home/adit/hadoop/bin/hadoop fs -appendToFile - /tshark_attack
 
        sudo /home/adit/hadoop/bin/hadoop jar /home/adit/Desktop/hadoop-streaming-2.8.3.jar -mapper /home/adit/Downloads/mapper1.py -reducer /home/adit/Downloads/reducer1.py -input /tsharka1 -output /attack_outputt
        sudo /home/adit/hadoop/bin/hadoop fs -cat /attack_outputt/part-00000 | /home/adit/hadoop/bin/hadoop fs -appendToFile - /attack_output/part-00000
        sudo /home/adit/hadoop/bin/hadoop fs -rmr /attack_outputt
    done   

    
