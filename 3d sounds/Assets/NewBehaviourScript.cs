using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;


public class NewBehaviourScript : MonoBehaviour {
 
    Camera mainCam;
    Byte[] bytes = new Byte[256];
    //string data = null;

    //int port = 13000;
    //IPAddress localAddr = IPAddress.Parse("127.0.0.1");
    //TcpListener server=null;

    TcpClient client;

	void Start () 
    {
      
        mainCam = Camera.main;
        //server = new TcpListener(localAddr, port);


    }


    float startTime = 0;
    string prevLine;

	 void Update()
	{



        string line = File.ReadAllText(@"/Users/kcpoduru/Desktop/hackathon/file.txt", Encoding.UTF8);
        if(float.Parse(line) == 1.0)
        {
            mainCam.transform.position = new Vector3(0, 0, 2000);
        
        }
        if (float.Parse(line) != 1.0 && prevLine !=line)
        {
            prevLine = line;
            startTime = Time.time;
            Debug.Log(line);
        }

        if( Time.time - startTime < 6)
        {
            mainCam.transform.position = new Vector3(float.Parse(line), -10, 0);

        }
        else
        {
            mainCam.transform.position = new Vector3(0, 0, 2000);
            File.WriteAllText(@"/Users/kcpoduru/Desktop/hackathon/file.txt", "1");
            prevLine = "1.0";
        }

    }






	//void krishna()
	//{
	//    while (true)
	//    {


	//        server.Start();
	//        Debug.Log("Waiting for a connection... ");
	//        client = server.AcceptTcpClient();
	//        Debug.Log("Connected!"); 
	//        data = null;
	//        NetworkStream stream = client.GetStream();
	//        int i;
	//        while ((i = stream.Read(bytes, 0, bytes.Length)) != 0)
	//        {

	//            data = System.Text.Encoding.ASCII.GetString(bytes, 0, i);
	//            Debug.Log("data is " + data);

	//        }

	//    }
	//}






	//  




}


