from tkinter import *
from GraphAlgo import *
from Graph import *







class RunGUI:
    #~~~~~~~~~~~` windows parameters ~~~~~~~~~~~~~~~~~~~~~~~~~#
    aTemp = GraphAlgo()
    GraphAlgorr = aTemp.GraphAlgoInstance()
    root = Tk()
    root.title('GUI - Python Directed Graph'+str(GraphAlgorr))
    root.geometry("1000x900")
    wwwidth = 1000
    hhheight = 900
    Can = Canvas(root, width=wwwidth, height=hhheight, bg="black")
    boolDijekstra = False
    boolTSP = False
    boolCenter = False
    boolLoad = False
    DijkstraPath = []

    MainGraph = DiGraph()
    MainGraphAlgo = GraphAlgo()

    #### ~~~~~~~~~ controls for input ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
    DijekstraSource = Entry(root,
                            bg="#CAFF70",
                            cursor="arrow",
                            fg="blue",
                            highlightcolor="black",
                            justify="right",
                            width=10,
                            xscrollcommand="scrollbar",
                            )
    DijekstraSource.pack()
    DijekstraSource.place(width=40, height=20, x=100)
    DijekstraDest = Entry(root,
                          bg="#CAFF70",
                          cursor="arrow",
                          fg="blue",
                          highlightcolor="black",
                          justify="right",
                          width=10,
                          xscrollcommand="scrollbar",

                          )
    DijekstraDest.pack()
    DijekstraDest.place(width=40, height=20, x=150)
    LoadFromPPPATHjson = Entry(root,
                               bg="#FFB6C1",
                               cursor="arrow",
                               fg="blue",
                               highlightcolor="black",
                               justify="right",
                               width=10,
                               xscrollcommand="scrollbar",
                               )
    LoadFromPPPATHjson.pack()
    LoadFromPPPATHjson.place(width=100, height=20, x=500)
    #####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def ShowGraph(self,GGraph:DiGraph()):
        ##~~~~~~~~~~~` basic canvas setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        self.Can.pack(pady=20)
        self.Can.create_line(0,self.hhheight/2,self.wwwidth,self.hhheight/2,fill="orange")
        self.Can.create_line(self.wwwidth/2,0,self.wwwidth/2,self.hhheight,fill="orange")
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        ## ~~~~~~~~~~~~~~~` draw th graph ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        TempNodeDic = GGraph.NodeDic
        TempEdgeDic = GGraph.EdgeSrcDic
        for items in TempNodeDic: ## ~~~~ Nodes first
            NodeX = int(   80000*(float(TempNodeDic.get(items).x)%0.01)   )
            NodeY = int(   80000*(float(TempNodeDic.get(items).y)%0.01)   )
            NodeXsize = NodeX+60
            NodeYsize = NodeY+60
            #print(str(NodeX)+"     "+str(NodeY))
            self.Can.create_oval(NodeX, NodeY,NodeXsize ,NodeYsize , width=3,outline="#FF1493",fill="#551A8B")
        for itemI in TempEdgeDic: ## ~~~~~~ then Edges
            for itemJ in TempEdgeDic.get(itemI):
                RealNodeX1 = TempEdgeDic.get(itemI).get(itemJ).Src.x
                RealNodeY1 = TempEdgeDic.get(itemI).get(itemJ).Src.y
                #print(str(RealNodeX1)+","+str(RealNodeY1))
                NodeX1 = int(80000 * (float(RealNodeX1) % 0.01))+30
                NodeY1 = int(80000 * (float(RealNodeY1) % 0.01))+30
                RealNodeX2 = TempEdgeDic.get(itemI).get(itemJ).Dest.x
                RealNodeY2 = TempEdgeDic.get(itemI).get(itemJ).Dest.y
                NodeX2 = int(80000 * (float(RealNodeX2) % 0.01))+30
                NodeY2 = int(80000 * (float(RealNodeY2) % 0.01))+30
                self.Can.create_line(NodeX1,NodeY1,NodeX2,NodeY2,arrow="last",width=5,fill="#3A5FCD")
        for items in TempNodeDic: ## ~~~~~ then Node Text
            NodeX = int(   80000*(float(TempNodeDic.get(items).x)%0.01)   )
            NodeY = int(   80000*(float(TempNodeDic.get(items).y)%0.01)   )
            self.Can.create_text(NodeX+30,NodeY+30,text = "Node "+str(TempNodeDic.get(items).id),fill="white", font=('Arial','8','bold'))
        self.Can.pack(pady=20)
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



        #####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ buttons setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
        buttonDije = Button(self.root, command=self.setDijekstra, text="Dijkstra", bg="grey", font=('Arial', '7', 'bold'))
        buttonTSP = Button(self.root, command=self.setTSP, text="TSP", bg="grey", font=('Arial', '7', 'bold'))
        buttonCenter = Button(self.root, command=self.setCenter, text="Center", bg="grey", font=('Arial', '7', 'bold'))
        buttonLoad = Button(self.root, command=self.LoadFromJSONButt, text="Load From", bg="grey", font=('Arial', '7', 'bold'))
        buttonLoad.pack()
        buttonTSP.pack()
        buttonCenter.pack()
        buttonDije.pack()
        buttonDije.place(width=70, height=20, x=10)
        buttonCenter.place(width=70, height=20, x=260)
        buttonTSP.place(width=70, height=20, x=340)
        buttonLoad.place(width=70, height=20, x=420)
        ###########~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
        if self.boolDijekstra==True:
            listTemp = self.DijkstraPath
            for i in range(0, len(listTemp) - 1):  ## ~~~~~~ then Edges
                #print(self.MainGraphAlgo.nGraph.EdgeSrcDic.get(listTemp[i]).get(listTemp[i+1]))
                RealNodeX1 = self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).x
                RealNodeY1 = self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).y
                # print(str(RealNodeX1)+","+str(RealNodeY1))
                NodeX1 = int(80000 * (float(RealNodeX1) % 0.01)) + 30
                NodeY1 = int(80000 * (float(RealNodeY1) % 0.01)) + 30
                RealNodeX2 = self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i+1]).x
                RealNodeY2 = self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i+1]).y
                NodeX2 = int(80000 * (float(RealNodeX2) % 0.01)) + 30
                NodeY2 = int(80000 * (float(RealNodeY2) % 0.01)) + 30
                self.Can.create_line(NodeX1, NodeY1, NodeX2, NodeY2, arrow="last", width=2, arrowshape=(15, 30, 15),
                                fill="#00FA9A")
                self.Can.pack()
            for i in range(0, len(listTemp)):  ## ~~~~ Nodes first
                NodeX = int(80000 * (float(self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).x) % 0.01))
                NodeY = int(80000 * (float(self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).y) % 0.01))
                NodeXsize = NodeX + 60
                NodeYsize = NodeY + 60
                # print(str(NodeX)+"     "+str(NodeY))
                self.Can.create_oval(NodeX, NodeY, NodeXsize, NodeYsize, width=3, outline="#00FA9A")
            for i in range(0, len(listTemp)):  ## ~~~~~ then Node Text
                NodeX = int(80000 * (float(self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).x) % 0.01))
                NodeY = int(80000 * (float(self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).y) % 0.01))-40
                self.Can.create_text(NodeX + 30, NodeY + 30, text="Dijkstra Path " + str(i),
                                     fill="#00FA9A", font=('Arial', '7', 'bold'))
            self.Can.pack(pady=20)
        if self.boolTSP==True:
            if self.MainGraphAlgo.CanIGetFromEveryNodeToAnyNode:
                listTemp = self.MainGraphAlgo.TSP(list(self.MainGraphAlgo.nGraph.NodeDic.keys()))[0]
                print(listTemp)
                for i in range(0, len(listTemp) - 1):  ## ~~~~~~ then Edges
                    # print(self.MainGraphAlgo.nGraph.EdgeSrcDic.get(listTemp[i]).get(listTemp[i+1]))
                    RealNodeX1 = self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).x
                    RealNodeY1 = self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).y
                    # print(str(RealNodeX1)+","+str(RealNodeY1))
                    NodeX1 = int(80000 * (float(RealNodeX1) % 0.01)) + 30
                    NodeY1 = int(80000 * (float(RealNodeY1) % 0.01)) + 30
                    RealNodeX2 = self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i + 1]).x
                    RealNodeY2 = self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i + 1]).y
                    NodeX2 = int(80000 * (float(RealNodeX2) % 0.01)) + 30
                    NodeY2 = int(80000 * (float(RealNodeY2) % 0.01)) + 30
                    self.Can.create_line(NodeX1, NodeY1, NodeX2, NodeY2, arrow="last", width=2, arrowshape=(15, 30, 15),
                                         fill="#E066FF")
                    self.Can.pack()
                for i in range(0, len(listTemp)):  ## ~~~~ Nodes first
                    NodeX = int(80000 * (float(self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).x) % 0.01))
                    NodeY = int(80000 * (float(self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).y) % 0.01))
                    NodeXsize = NodeX + 60
                    NodeYsize = NodeY + 60
                    # print(str(NodeX)+"     "+str(NodeY))
                    self.Can.create_oval(NodeX, NodeY, NodeXsize, NodeYsize, width=3, outline="#E066FF")
                for i in range(0, len(listTemp)):  ## ~~~~~ then Node Text
                    NodeX = int(80000 * (float(self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).x) % 0.01))
                    NodeY = int(80000 * (float(self.MainGraphAlgo.nGraph.NodeDic.get(listTemp[i]).y) % 0.01)) - 40
                    self.Can.create_text(NodeX + 30, NodeY + 30, text="TSP Path " + str(i),
                                         fill="#E066FF", font=('Arial', '7', 'bold'))
                self.Can.pack(pady=20)
        if self.boolCenter==True:
            CenterNode = self.MainGraphAlgo.centerPoint()
            print(CenterNode)
            NodeX = int(80000 * (float(self.MainGraphAlgo.nGraph.NodeDic.get(CenterNode[0]).x) % 0.01))
            NodeY = int(80000 * (float(self.MainGraphAlgo.nGraph.NodeDic.get(CenterNode[0]).y) % 0.01))
            NodeXsize = NodeX + 60
            NodeYsize = NodeY + 60
            # print(str(NodeX)+"     "+str(NodeY))
            self.Can.create_oval(NodeX, NodeY, NodeXsize, NodeYsize, width=3, outline="Yellow")
            self.Can.create_text(NodeX+30, NodeY -30, text="Center",
                                 fill="Yellow", font=('Arial', '7', 'bold'))
            self.Can.pack(pady=20)
        if self.boolLoad == False:
            self.Can.pack(pady=20)
            self.Can.create_rectangle(0,0,3000,3000,fill="black")
            self.Can.create_line(0, self.hhheight / 2, self.wwwidth, self.hhheight / 2, fill="orange")
            self.Can.create_line(self.wwwidth / 2, 0, self.wwwidth / 2, self.hhheight, fill="orange")
        #print(self.MainGraphAlgo.nGraph.OperationsMC )
        self.MainGraphAlgo.nGraph = GGraph
        self.root.mainloop()
    def setDijekstra(self):
        if self.boolDijekstra == False:
            self.boolDijekstra = True
            SSSource = 0
            DDDest = 0
            if self.DijekstraSource.get() != None:
                SSSource = self.DijekstraSource.get()
            if self.DijekstraDest.get() != None:
                DDDest = self.DijekstraDest.get()
            tupleDij = self.MainGraphAlgo.shortest_path(int(SSSource), int(DDDest))
            print(tupleDij)
            self.DijkstraPath = tupleDij[1]
            self.ShowGraph(self.MainGraphAlgo.nGraph)
        else:
            self.boolDijekstra = False
            self.Can.delete('all')
            self.ShowGraph(self.MainGraphAlgo.nGraph)
    def setTSP(self):
        if self.boolTSP == False:
            self.boolTSP = True
            self.ShowGraph(self.MainGraphAlgo.nGraph)
        else:
            self.boolTSP = False
            self.Can.delete('all')
            self.ShowGraph(self.MainGraphAlgo.nGraph)
    def setCenter(self):
        if self.boolCenter == False:
            self.boolCenter = True
            self.ShowGraph(self.MainGraphAlgo.nGraph)
        else:
            self.boolCenter = False
            self.Can.delete('all')
            self.ShowGraph(self.MainGraphAlgo.nGraph)
    def LoadFromJSONButt(self):
        if self.boolLoad == False:
            self.boolLoad = True
            self.Can.delete('all')
            self.MainGraphAlgo = None
            self.MainGraphAlgo = GraphAlgo()
            self.MainGraphAlgo.load_from_json(self.LoadFromPPPATHjson.get())
            self.ShowGraph(self.MainGraphAlgo.nGraph)
        else:
            self.boolLoad = False
            self.Can.delete('all')
            self.ShowGraph(self.MainGraphAlgo.nGraph)