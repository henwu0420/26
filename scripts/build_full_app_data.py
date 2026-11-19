# scripts/build_full_app_data.py
# -*- coding: utf-8 -*-
import json

with open('site_assets/mcqs_enriched.json', 'r', encoding='utf-8') as f:
    mcqs = json.load(f)

# Non-MCQ Data Definitions
non_mcq_data = {
    "ch3": {
        "fill_ins": [
            {
                "title": "1. 電腦五大單元（馮紐曼架構）功能對照表",
                "headers": ["組成單元", "英文縮寫", "核心功能", "硬體實例"],
                "rows": [
                    ["控制單元", "CU", "控制及協調電腦各單元間的運作（如指令解碼、控制訊號發布）", "CPU 內部控制邏輯電路"],
                    ["算術／邏輯單元", "ALU", "負責資料的運算（加減乘除）與邏輯判斷（大於、小於、AND、OR）", "CPU 內部運算核心"],
                    ["記憶單元", "MU", "電腦存放程式與資料的地方（包含主記憶體與輔助記憶體）", "RAM、ROM、SSD、硬碟"],
                    ["輸入單元", "IU", "電腦接受指令及輸入資料的管道（外界 ➔ 電腦）", "鍵盤、滑鼠、掃描器、麥克風"],
                    ["輸出單元", "OU", "電腦輸出運算結果的管道（電腦 ➔ 外界）", "螢幕、印表機、喇叭、投影機"]
                ],
                "note": "★ 重點叮嚀：輸入單元（IU）與輸出單元（OU）合稱為『週邊設備（I/O Devices）』；控制單元（CU）與算術邏輯單元（ALU）加上暫存器合稱為『中央處理器（CPU）』。"
            },
            {
                "title": "2. CPU 機器週期（Machine Cycle）四大步驟",
                "steps": [
                    {"step": "1. 擷取（Fetch）", "stage": "擷取週期（Instruction Cycle）", "detail": "由控制單元（CU）根據程式計數器（PC）所指的記憶體位址，從主記憶體中取出指令，載入指令暫存器（IR）。"},
                    {"step": "2. 解碼（Decode）", "stage": "擷取週期（Instruction Cycle）", "detail": "由控制單元（CU）分析解讀指令暫存器中的運算碼（Opcode），確認要執行何種操作。"},
                    {"step": "3. 執行（Execute）", "stage": "執行週期（Execution Cycle）", "detail": "由算術邏輯單元（ALU）依據解碼結果，執行加減乘除或邏輯運算。"},
                    {"step": "4. 儲存（Store）", "stage": "執行週期（Execution Cycle）", "detail": "將 ALU 運算後的結果存回累加器（ACC）或寫入主記憶體中。"}
                ],
                "note": "★ 考前速記：機器週期 ＝ 擷取 ➔ 解碼 ➔ 執行 ➔ 儲存（Fetch ➔ Decode ➔ Execute ➔ Store）。前兩步為擷取週期，後兩步為執行週期！"
            },
            {
                "title": "3. 主記憶體雙雄對比：DRAM（動態RAM） vs SRAM（靜態RAM）",
                "headers": ["比較項目", "動態隨機存取記憶體（DRAM）", "靜態隨機存取記憶體（SRAM）"],
                "rows": [
                    ["內部基本元件", "電容器（Capacitor） ＋ 單顆電晶體", "正反器（Flip-Flop，多顆電晶體）"],
                    ["是否需週期性充電", "是（電容會自然漏電，需持續 Refresh）", "否（通電期間資料永不消失，不需充電）"],
                    ["存取速度", "較慢（約數十奈秒 ns）", "極快（約數奈秒 ns）"],
                    ["積集度（單位面積容量）", "極高（結構簡單，可在小晶片做大容量）", "較低（結構複雜，佔用晶片面積大）"],
                    ["單位儲存價格", "便宜（性價比高）", "極貴（製造成本高昂）"],
                    ["主要實際應用", "個人電腦之『主記憶體』（如 DDR4 / DDR5）", "CPU 內部的『快取記憶體』（L1 / L2 / L3 Cache）"]
                ],
                "note": "★ 必背口訣：SRAM 快、貴、不充電、做快取；DRAM 慢、平、要充電、做主存。"
            },
            {
                "title": "4. 噴墨印表機混色色彩模式",
                "content": "噴墨印表機是藉由 <b>CMYK</b> 四色墨水的混合調配，來呈現出自然界中絕大部分的豐富色彩：\n- <b>C（Cyan，青色）</b>\n- <b>M（Magenta，洋紅色）</b>\n- <b>Y（Yellow，黃色）</b>\n- <b>K（blacK / Key，黑色）</b>\n（註：螢幕顯示採用色光三原色 RGB 加色法；彩色印刷與噴墨採用色料三原色 CMYK 減色法）。"
            },
            {
                "title": "5. 常見印表機類別與技術規格大PK",
                "headers": ["分類類別", "印表機種類", "列印原理", "速度評級", "主要耗材", "最佳應用場合"],
                "rows": [
                    ["撞擊式", "點陣式印表機", "撞針撞擊色帶在紙上打印出點陣文字", "較慢", "色帶（Ribbon）", "複寫紙、多聯式發票、快遞單、報表紙"],
                    ["非撞擊式", "噴墨印表機", "微細噴嘴將微滴墨水精準噴在紙張上", "中等", "墨水匣、噴嘴頭", "相片洗印、家庭彩色列印、海報印刷"],
                    ["非撞擊式", "雷射印表機", "雷射光束照射感光鼓靜電吸附碳粉加熱定影", "極快", "碳粉匣（Toner）、感光鼓", "學校或企業大量黑白/彩色文件、合約快速列印"]
                ],
                "note": "★ 重要單位考點：印表機列印速度單位為 <b>ppm</b>（每分鐘頁數）；列印解析度單位為 <b>dpi</b>（每英吋點數）。"
            }
        ],
        "practices": [
            {
                "title": "三、多元練習 1：主機板組件插槽與代號配對",
                "image": "site_assets/images/p4_8_Im1.png",
                "description": "下圖為電腦主機板核心插槽分布圖，請寫出各標號對應之安插組件：",
                "matches": [
                    {"slot": "A 插槽", "component": "戊、顯示卡", "detail": "PCI-Express x16 高速擴充插槽，專門安裝獨立顯示卡。"},
                    {"slot": "B 插槽", "component": "丙、硬碟", "detail": "SATA 傳輸埠或 M.2 插槽，用於連接 SSD 或傳統機械硬碟。"},
                    {"slot": "C 插槽", "component": "甲、CPU", "detail": "CPU 處理器插槽（Socket），中央核心運算大腦所在處。"},
                    {"slot": "D 插槽", "component": "乙、記憶體", "detail": "DIMM 記憶體插槽，安裝 DDR4 / DDR5 主記憶體條。"},
                    {"slot": "E 插槽", "component": "丁、電源供應器", "detail": "ATX 24-Pin 主電源插座，連接電源供應器供應全板電力。"}
                ]
            },
            {
                "title": "三、多元練習 2：生活情境科技設備精準選用",
                "problems": [
                    {"scenario": "(1) 小藍常需攜帶大量資料展示給客戶看，她可以購買哪一項設備來儲存資料？", "ans": "d. 隨身碟", "reason": "隨身碟具備 USB 介面、快閃記憶體晶片，體積小容量大、隨插即用，極便於外出攜帶。"},
                    {"scenario": "(2) 網路報稅提供用健保卡登入身分的功能，阿香需要哪一項設備，才能使用此功能報稅？", "ans": "b. 晶片讀卡機", "reason": "健保卡與自然人憑證皆為接觸式晶片卡，必須使用晶片讀卡機（Smart Card Reader）讀取晶片資訊。"},
                    {"scenario": "(3) 小盧要去戶外郊遊，為了避免手機沒電，他可以攜帶哪一項設備來提供手機電力？", "ans": "g. 行動電源", "reason": "行動電源（Power Bank）內建大容量鋰電池，可在無市電戶外隨時透過傳輸線為智慧型手機充電。"},
                    {"scenario": "(4) 老王購買了有趣的虛擬實境遊戲，請問他需要哪一項設備，才能體驗身歷其境的感受？", "ans": "c. 頭戴式VR裝置", "reason": "VR 頭戴式顯示器（VR Headset）能追蹤頭部視角並呈現 360 度 3D 沉浸式虛擬視野。"}
                ]
            }
        ],
        "worksheets": [
            {
                "title": "四、學習單：電腦配備升級與相容性診斷（加分題）",
                "description": "想讓家中的舊電腦戰力飆升，更換新硬體時必須注意主機板的規格與相容性！",
                "components": [
                    {"name": "中央處理器（CPU）", "key_spec": "核心數、時脈頻率、腳位規格（Socket）", "check": "需檢查主機板 CPU 腳座規格（如 LGA1700 或 AM5）是否相容。"},
                    {"name": "主記憶體（RAM）", "key_spec": "容量（16GB/32GB）、頻率（DDR4/DDR5）", "check": "需檢查主機板支援的 DDR 世代與插槽數量上限。"},
                    {"name": "固態硬碟（SSD）", "key_spec": "介面規格（M.2 PCIe 4.0 NVMe）、容量（1TB）", "check": "檢查主機板是否具有高速 M.2 NVMe 插槽。"},
                    {"name": "獨立顯示卡（GPU）", "key_spec": "顯示記憶體（VRAM）、PCIe 規格、功耗瓦數", "check": "需檢查電源供應器瓦數（PSU）是否充足，機殼長度是否容納得下。"}
                ]
            }
        ]
    },
    "ch4": {
        "fill_ins": [
            {
                "title": "1. 電腦軟體全方位分類樹狀結構",
                "structure": {
                    "系統軟體（System Software）": [
                        "<b>作業系統（OS）</b>：分派與管理電腦軟、硬體的資源（如 Windows, Linux, macOS, Android, iOS）。",
                        "<b>公用程式（Utilities）</b>：維護與支援電腦的運作（如 磁碟清理、磁碟重組、修復磁碟機、防毒軟體、驅動程式備份）。",
                        "<b>語言翻譯程式（Translators）</b>：將使用者撰寫的高階程式語言轉換成電腦可執行的機器語言（如 編譯器 Compiler、直譯器 Interpreter）。"
                    ],
                    "應用軟體（Application Software）": [
                        "<b>套裝軟體（Packaged Software）</b>：為大多數使用者的通用需求而設計公開發行（如 Office, Photoshop, 瀏覽器）。",
                        "<b>專案開發軟體（Custom Software）</b>：為特定對象或企業獨特業務需求而客製化設計（如 麥當勞POS系統、藏壽司全自動點餐、大台北公車查詢、學校校務行政系統）。"
                    ]
                }
            },
            {
                "title": "2. 六大主流作業系統特性超級比一比",
                "headers": ["作業系統", "開發維護者", "是否開放原始碼", "主要適用設備", "工作模式特性"],
                "rows": [
                    ["Windows", "微軟（Microsoft）", "否（商業閉源）", "個人電腦、筆電、平板", "單人多工（個人主機主流）"],
                    ["UNIX", "美國貝爾實驗室", "否（閉源專利）", "大型主機、伺服器、工作站", "多人多工（以 C 語言開發）"],
                    ["Linux", "Linux 基金會與開源社群", "是（開源自由軟體）", "伺服器、超級電腦、嵌入式", "多人多工（分支版本豐富如 Ubuntu, RedHat）"],
                    ["macOS", "蘋果公司（Apple）", "否（商業閉源）", "蘋果 Mac 系列個人電腦", "單人多工（以 UNIX 為底層）"],
                    ["Android", "Google 公司", "是（開放原始碼專案）", "智慧型手機、平板、智慧電視", "單人多工（市佔第一行動系統）"],
                    ["iOS", "蘋果公司（Apple）", "否（封閉生態系）", "iPhone 智慧型手機", "單人多工（限定 App Store 下載）"]
                ]
            },
            {
                "title": "3. 作業系統工作模式三大分類",
                "headers": ["分類類別", "核心定義", "典型代表作業系統"],
                "rows": [
                    ["單人單工", "同一時間內僅允許單一使用者執行單一任務", "MS-DOS"],
                    ["單人多工", "同一時間內允許單一使用者同時執行多個應用程式視窗", "Windows、macOS、Android、iOS"],
                    ["多人多工", "同一時間內允許多位使用者透過連線登入，各自同時執行多項程式", "UNIX、Linux、Windows Server"]
                ]
            },
            {
                "title": "4. 雲端運算資源三層服務架構（IaaS / PaaS / SaaS）",
                "headers": ["服務模式", "英文全稱", "租用內容與提供資源", "服務提供商代表實例"],
                "rows": [
                    ["IaaS", "Infrastructure as a Service<br>基礎建設即服務", "租用硬體基礎設施：虛擬伺服器、儲存空間、虛擬網路。不需自行購置機房主機。", "AWS EC2 / S3、Google Cloud Compute Engine、微軟 Azure VM"],
                    ["PaaS", "Platform as a Service<br>平台即服務", "租用軟體開發與執行平台：作業系統、資料庫管理系統、程式運行環境。開發者直接寫程式部屬。", "Google App Engine、Oracle Cloud PaaS、Heroku、AWS Elastic Beanstalk"],
                    ["SaaS", "Software as a Service<br>軟體即服務", "終端使用者直接透過瀏覽器或 App 使用現成應用軟體，免安裝免維護。", "LINE、Google 文件 / Gmail、YouTube、Office 365、Netflix"]
                ],
                "note": "★ 考前記憶心法：IaaS ＝ 租毛胚屋（硬體空間）；PaaS ＝ 租精裝房自帶廚具（開發平台）；SaaS ＝ 住五星級飯店享現成服務（直接用軟體）。"
            }
        ],
        "practices": [
            {
                "title": "三、多元練習 1：軟體類型精準歸類配對",
                "problems": [
                    {"name": "(1) macOS", "code": "a. 作業系統", "detail": "管理 Mac 蘋果電腦硬體核心，屬於系統軟體中的作業系統。"},
                    {"name": "(2) Photoshop", "code": "d. 套裝軟體", "detail": "公開販售供廣大大眾影像編修的現成應用軟體。"},
                    {"name": "(3) 麥當勞專用的 POS（銷售點）系統", "code": "e. 專案開發軟體", "detail": "專為麥當勞連鎖點餐櫃檯結帳流程量身客製的應用軟體。"},
                    {"name": "(4) 磁碟清理工具", "code": "b. 公用程式", "detail": "維護磁碟空間清理暫存檔的系統輔助軟體。"},
                    {"name": "(5) 編譯器（Compiler）", "code": "c. 語言翻譯程式", "detail": "將高階程式碼一次翻譯成機器語言的系統軟體。"}
                ]
            },
            {
                "title": "三、多元練習 2：作業系統情境特點填空",
                "problems": [
                    {"desc": "(1) 採取開放原始碼的做法，常作為網路作業系統。", "ans": "b. Linux", "why": "開源自由且網路伺服器穩定度極佳。"},
                    {"desc": "(2) 微軟公司開發的作業系統。", "ans": "a. Windows", "why": "全球桌面 PC 市佔率第一的微軟作業系統。"},
                    {"desc": "(3) 適用於 iPhone、iPad 的作業系統。", "ans": "c. iOS", "why": "蘋果行動裝置專用封閉系統。"}
                ]
            }
        ],
        "worksheets": [
            {
                "title": "四、學習單：資訊科技名詞填字遊戲（Crossword Puzzle）完整正解",
                "horizontal": [
                    {"num": "1", "hint": "區域網路的英文縮寫", "ans": "LAN", "note": "Local Area Network"},
                    {"num": "2", "hint": "微軟公司開發的多工作業系統", "ans": "WINDOWS", "note": "微軟招牌 OS"},
                    {"num": "3", "hint": "由 Google 公司開發，許多智慧型手機所採用的作業系統", "ans": "ANDROID", "note": "非蘋陣營首選"},
                    {"num": "4", "hint": "基礎建設即服務的英文縮寫", "ans": "IAAS", "note": "Infrastructure as a Service"},
                    {"num": "5", "hint": "平台即服務的英文縮寫", "ans": "PAAS", "note": "Platform as a Service"},
                    {"num": "6", "hint": "免費的瀏覽器軟體", "ans": "CHROME", "note": "Google 開發之全球主流瀏覽器"}
                ],
                "vertical": [
                    {"num": "一", "hint": "麥金塔的英文縮寫", "ans": "MAC", "note": "Macintosh 縮寫"},
                    {"num": "二", "hint": "以 UNIX 為基礎所發展的開源作業系統", "ans": "LINUX", "note": "由 Linus 發起"},
                    {"num": "三", "hint": "軟體即服務的英文縮寫", "ans": "SAAS", "note": "Software as a Service"},
                    {"num": "四", "hint": "圖形使用者介面的英文縮寫", "ans": "GUI", "note": "Graphical User Interface"},
                    {"num": "五", "hint": "開發蘋果電腦的公司", "ans": "APPLE", "note": "蘋果公司"},
                    {"num": "六", "hint": "網際網路的英文", "ans": "INTERNET", "note": "全球網路集合體"},
                    {"num": "七", "hint": "作業系統的英文縮寫", "ans": "OS", "note": "Operating System"}
                ]
            }
        ]
    },
    "ch5": {
        "fill_ins": [
            {
                "title": "1. 系統平台運作標準三步驟（IPO模型）",
                "content": "系統平台運作的流程主要包含三大核心步驟：\n1. <b>輸入（Input）</b>：透過鍵盤、滑鼠、感測器或傳輸媒介將外界資料輸入至系統中。\n2. <b>處理（Process）</b>：系統利用微處理器（CPU/GPU）執行邏輯運算與資料轉換。\n3. <b>輸出（Output）</b>：將處理完成的有用資訊傳送至螢幕、印表機、儲存設備或雲端空間。"
            },
            {
                "title": "2. Windows 檔案屬性之控制與管理",
                "content": "- <b>檢視工具</b>：在 Windows 中可透過『<b>檔案總管</b>』視窗檢視與組織管理電腦中的資料夾與檔案。\n- <b>常見檔案屬性</b>：\n  * <b>唯讀（Read-Only）</b>：設定後只能讀取檢視檔案內容，不能被修改或刪除，可保護關鍵檔案防誤刪。\n  * <b>隱藏（Hidden）</b>：設定後系統預設將其隱藏不顯示在目錄中。若要查看，需點選上方『檢視』➔ 勾選『隱藏的項目』。"
            },
            {
                "title": "3. 平行處理（Parallel Processing）定義",
                "content": "<b>平行處理</b>是指將要進行的大型計算工作，切割分解成數個獨立或關聯的部分，分別交給多個處理器（或多核心 CPU 中的各個核心）同時進行運算，以成倍加快處理速度。"
            },
            {
                "title": "4. 程序五大狀態機轉換圖與時機全解析",
                "states": [
                    {"name": "建立（New）", "desc": "程序正在被作業系統建立，配置 PCB（程序控制表），等待進入記憶體。"},
                    {"name": "就緒（Ready）", "desc": "程序已載入主記憶體，一切資源備妥，單純等待 CPU 排程器挑選調度。"},
                    {"name": "執行（Running）", "desc": "程序正式獲得 CPU，指令正在處理器中高速執行。"},
                    {"name": "等待（Waiting / Blocked）", "desc": "執行中因需要等待 I/O 輸入輸出操作（如等待磁碟讀檔、等鍵盤按鍵）或特定事件發生而暫停執行釋出 CPU。"},
                    {"name": "結束（Terminated）", "desc": "程序執行完畢，作業系統回收記憶體與相關系統資源。"}
                ],
                "transitions": [
                    "<b>就緒 ➔ 執行</b>：CPU 排程器選中該程序（Dispatch）。",
                    "<b>執行 ➔ 就緒</b>：時間片段用盡（Time-out）或被更高優先順序程序插隊中斷（Interrupt）。",
                    "<b>執行 ➔ 等待</b>：發出 I/O 請求或等待事件。",
                    "<b>等待 ➔ 就緒</b>：I/O 動作完成，回到就緒佇列排隊等 CPU。"
                ]
            },
            {
                "title": "5. 三大經典 CPU 工作排程演算法比較",
                "headers": ["排程演算法", "英文縮寫", "核心排程原則", "優點與特點", "致命缺點與解決之道"],
                "rows": [
                    ["先來先服務", "FCFS<br>(First-Come First-Served)", "依照程序進入就緒佇列的先後順序依序處理", "公平、演算法邏輯最簡單", "若長工作排在最前面，會導致後方短工作大排長龍（稱為護航效應 Convoy Effect）"],
                    ["最短工作優先", "SJF<br>(Shortest Job First)", "先預測或判斷 CPU 處理時間，處理時間愈短者愈先執行", "能達到理論上最小的平均等待時間", "長工作若遇到連續短工作插隊，可能會長時間無法執行"],
                    ["優先排程", "PS<br>(Priority Scheduling)", "每個程序賦予一個優先權等級，優先權愈高者愈先處理", "能保證關鍵緊急任務第一時間搶先執行", "<b>飢餓現象（Starvation）</b>：低優先度工作可能被無限期擱置！解法為<b>老化技術（Aging）</b>隨等待時間調升優先級"]
                ]
            }
        ],
        "practices": [
            {
                "title": "三、多元練習 1：Windows 工作管理員介面圖表實作判讀",
                "image": "site_assets/images/p13_20_Im1.png",
                "questions": [
                    {"q": "(1) 請從效能圖表讀出：CPU使用率為多少？記憶體使用率為多少？", "ans": "CPU 使用率為 <b>3%</b>；記憶體使用率為 <b>25%</b>。"},
                    {"q": "(2) 該台電腦安裝的主記憶體實體總容量共有多少？", "ans": "共有 <b>16 GB</b>。"},
                    {"q": "(3) 若想檢視目前正在背景執行的所有應用程式與程序清單，應點擊哪一個標籤？", "ans": "點擊『<b>處理程序</b>』標籤。"}
                ]
            }
        ],
        "worksheets": [
            {
                "title": "四、學習單：Google Teachable Machine 機器學習實驗原理",
                "image": "site_assets/images/p14_22_Im1.png",
                "concepts": [
                    {
                        "q": "(1) 機器所蒐集到的圖片樣本越多，圖片辨識效果是越好還是越差？",
                        "ans": "<b>愈好</b>",
                        "reason": "機器學習依賴海量訓練資料，樣本數量越多、角度光影越豐富，演算法越能萃取出具代表性的特徵權重，辨識準確率便越高。"
                    },
                    {
                        "q": "(2) 訓練週期數（Epochs）越大還是越小，模型越能學會圖片辨識？",
                        "ans": "<b>愈大</b>",
                        "reason": "訓練週期數（Epochs）代表整個訓練數據集被神經網絡反覆學習的完整次數，週期數適度增加能讓神經網路持續調整權重減少誤差，使模型越能學會特徵辨識。"
                    }
                ]
            }
        ]
    },
    "ch6": {
        "fill_ins": [
            {
                "title": "1. 辦公室應用軟體三大主力定義",
                "items": [
                    {"name": "文書處理軟體（Word Processor）", "def": "具有文字編輯、段落排版、表格製作、圖片置入、版面設定與頁首頁尾功能，專門用來輸入文稿、編排圖文並茂的正式報告與論文（如 Word, Writer, Pages）。"},
                    {"name": "電子試算表軟體（Spreadsheet）", "def": "具有資料計算、數學統計函數（SUM/AVERAGE）、資料排序、多條件篩選、樞紐分析與自動產出統計圖表功能，適合用來編製財務報表、成績冊與統計表單（如 Excel, Calc, Numbers）。"},
                    {"name": "簡報設計軟體（Presentation）", "def": "具備幻燈片版面配置、視覺化圖形設計、轉場特效動畫與演講者備忘稿功能，專門用於公開演講、課堂報告與商業提案展示（如 PowerPoint, Impress, Keynote）。"}
                ]
            },
            {
                "title": "2. 五大主流辦公室軟體套件對照大表（必考精華）",
                "headers": ["軟體套件家族", "文書處理", "電子試算表", "簡報設計", "資料庫管理", "授權性質"],
                "rows": [
                    ["Microsoft Office", "Word", "Excel", "PowerPoint", "Access", "商業版權軟體（微軟開發）"],
                    ["LibreOffice", "Writer", "Calc", "Impress", "Base", "免費自由開源軟體（社群維護）"],
                    ["Apache OpenOffice", "Writer", "Calc", "Impress", "Base", "免費開源軟體（Apache基金會）"],
                    ["Google 文件套件", "Google 文件 (Docs)", "Google 試算表 (Sheets)", "Google 簡報 (Slides)", "－（無獨立DBMS）", "雲端 SaaS 服務（瀏覽器免費使用）"],
                    ["Apple iWork", "Pages", "Numbers", "Keynote", "－", "蘋果生態系商業軟體（Apple原生）"]
                ],
                "note": "★ 考前配對心法：Word＝Writer＝Pages＝文件；Excel＝Calc＝Numbers＝試算表；PowerPoint＝Impress＝Keynote＝簡報！"
            },
            {
                "title": "3. 影像處理（Image Processing）定義與手法",
                "content": "影像（Image）是物體在腦中呈現的圖像。我們常為了<b>美化外觀、凸顯主題、修正瑕疵、便於網路傳輸或減少檔案容量</b>等目的，使用專用軟體（如 Photoshop, PhotoImpact, GIMP）對點陣圖片進行<b>去背、修斑、調色、濾鏡特效、縮圖壓縮與多圖合成</b>，這些作業通稱為『影像處理』。"
            }
        ],
        "practices": [
            {
                "title": "三、多元練習：多媒體設計師自修書單挑選",
                "description": "筱如未來想從事多媒體設計工作（需具備：影像處理、音樂剪輯、影片編輯、動畫製作）。請從下列書單挑選出適合的自修書籍：",
                "options": [
                    {"num": "(1)", "title": "超圖解 iPhone App 開發入門", "suitable": False, "reason": "屬於行動 App 程式設計開發，非多媒體後製設計。"},
                    {"num": "(2)", "title": "Excel 效率 UP！快速完成工作的技巧", "suitable": False, "reason": "屬於辦公室試算表數據處理，非多媒體設計。"},
                    {"num": "(3)", "title": "抓住你的 Photoshop", "suitable": True, "reason": "【正確勾選】Photoshop 為業界標準影像處理與合成修圖軟體。"},
                    {"num": "(4)", "title": "16 堂課成為 Maya 高手", "suitable": True, "reason": "【正確勾選】Maya 為好萊塢頂級 3D 動畫與角色建模軟體。"},
                    {"num": "(5)", "title": "必學！Python 資料科學‧機器學習", "suitable": False, "reason": "屬於後端程式語言與 AI 資料分析，非多媒體創作。"},
                    {"num": "(6)", "title": "Windows 使用手冊", "suitable": False, "reason": "作業系統日常操作指南。"},
                    {"num": "(7)", "title": "會聲會影～剪輯你的影片", "suitable": True, "reason": "【正確勾選】會聲會影為經典影片編輯剪輯後製軟體。"},
                    {"num": "(8)", "title": "電競電腦選購、組裝、應用", "suitable": False, "reason": "硬體硬體零組件組裝採購知識。"},
                    {"num": "(9)", "title": "聲音魔法師入門－Audacity", "suitable": True, "reason": "【正確勾選】Audacity 為開源多軌音樂剪輯、降噪與聲音特效軟體。"},
                    {"num": "(10)", "title": "讓我們 LINE 在一起！", "suitable": False, "reason": "通訊通訊軟體日常社交應用。"}
                ],
                "summary": "★ 正確勾選清單：(3) Photoshop、(4) Maya、(7) 會聲會影、(9) Audacity！"
            }
        ],
        "worksheets": [
            {
                "title": "四、學習單：Audacity 音樂剪輯手機鈴聲實作",
                "steps": [
                    "1. 下載並安裝 Audacity 免費開源音樂剪輯軟體。",
                    "2. 匯入 MP3 音樂檔案，利用選取工具標記副歌精華片段（約 40 秒），執行修剪與淡入淡出（Fade in / Fade out）。",
                    "3. 匯出為新音訊檔，透過傳輸線或雲端傳送至手機設定為來電鈴聲。"
                ],
                "qa": [
                    {"q": "(1) 所剪輯的音樂名稱為何？", "a": "看見愛情"},
                    {"q": "(2) 擷取音樂的哪一部分歌詞？", "a": "『說愛你 沒人不想聽 / 說恨你 卻總找不到理由 / 兩個都是我 Hey / 說想你 你已無法聽 / 這句話 紀念愛情曾來過 / 回憶在這 等我』"},
                    {"q": "(3) 擷取後的音樂播放總長度為多少秒？", "a": "40 秒（手機來電鈴聲最佳長度通常在 30~45 秒內）"},
                    {"q": "(4) 如何將音樂傳送到手機中？", "a": "使用 USB 手機傳輸線連接電腦與手機，或上傳至 Google Drive 雲端硬碟再於手機下載。"}
                ]
            }
        ]
    }
}

full_data = {
    "user_info": {
        "name": "高于翔",
        "student_id": "26",
        "class_name": "資處科一仁",
        "school_subject": "數位科技概論（上）",
        "textbook": "旗立資訊 數位科技概論 (C221A3系列)",
        "exam_scope": "第 3 章 ～ 第 6 章 期末總複習"
    },
    "statistics": {
        "total_mcqs": len(mcqs),
        "total_ch3": len([q for q in mcqs if q['chapter'] == 3]),
        "total_ch4": len([q for q in mcqs if q['chapter'] == 4]),
        "total_ch5": len([q for q in mcqs if q['chapter'] == 5]),
        "total_ch6": len([q for q in mcqs if q['chapter'] == 6]),
        "total_starred": len([q for q in mcqs if q.get('is_starred')]),
        "total_exercise_mcqs": len([q for q in mcqs if '習作本' in q['source']]),
        "total_quiz_mcqs": len([q for q in mcqs if '隨堂測驗卷' in q['source']])
    },
    "mcqs": mcqs,
    "non_mcq_data": non_mcq_data
}

# Write JS file for front-end
with open('site_assets/study_data.js', 'w', encoding='utf-8') as f:
    f.write('const STUDY_DATA = ')
    json.dump(full_data, f, ensure_ascii=False, indent=2)
    f.write(';\n')

print("Successfully written site_assets/study_data.js!")
