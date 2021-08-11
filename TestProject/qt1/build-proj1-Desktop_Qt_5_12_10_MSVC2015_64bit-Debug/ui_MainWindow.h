/********************************************************************************
** Form generated from reading UI file 'MainWindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.10
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionExit;
    QAction *actionSettings;
    QAction *actionMicOn;
    QAction *actionMicOff;
    QAction *actionPlay;
    QAction *actionStop;
    QAction *actionPause;
    QAction *actionDebugTest1;
    QAction *actionDebugTest2;
    QWidget *centralwidget;
    QGridLayout *gridLayout_3;
    QFrame *frame_2;
    QFormLayout *formLayout;
    QFrame *frame;
    QGridLayout *gridLayout;
    QTabWidget *tabWidget;
    QWidget *tabMain;
    QGridLayout *gridLayout_2;
    QFrame *frame_5;
    QGridLayout *gridLayout_4;
    QSplitter *splitter;
    QFrame *frame_3;
    QGridLayout *gridLayout_5;
    QTreeWidget *treeWidget1;
    QFrame *frame_4;
    QGridLayout *gridLayout_6;
    QTableWidget *tableWidget1;
    QWidget *tabDebug;
    QGridLayout *gridLayout_7;
    QFrame *frame_8;
    QGridLayout *gridLayout_9;
    QFrame *frame_6;
    QGridLayout *gridLayout_10;
    QLabel *label1;
    QPushButton *pushButton_2;
    QPushButton *pushButtonAddRow;
    QFrame *frame_7;
    QGridLayout *gridLayout_8;
    QTextEdit *textEditDebug1;
    QSpacerItem *verticalSpacer;
    QMenuBar *menubar;
    QMenu *menuFile;
    QStatusBar *statusbar;
    QToolBar *toolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1044, 803);
        QSizePolicy sizePolicy(QSizePolicy::Maximum, QSizePolicy::Maximum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        actionExit = new QAction(MainWindow);
        actionExit->setObjectName(QString::fromUtf8("actionExit"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/res/Resources/Icons/Cancel.ico"), QSize(), QIcon::Normal, QIcon::Off);
        actionExit->setIcon(icon);
        actionSettings = new QAction(MainWindow);
        actionSettings->setObjectName(QString::fromUtf8("actionSettings"));
        actionSettings->setCheckable(false);
        actionSettings->setChecked(false);
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/res/Resources/Icons/Gear.ico"), QSize(), QIcon::Normal, QIcon::Off);
        actionSettings->setIcon(icon1);
        actionMicOn = new QAction(MainWindow);
        actionMicOn->setObjectName(QString::fromUtf8("actionMicOn"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/res/Resources/Icons/Microphone_Green.ico"), QSize(), QIcon::Normal, QIcon::Off);
        actionMicOn->setIcon(icon2);
        actionMicOff = new QAction(MainWindow);
        actionMicOff->setObjectName(QString::fromUtf8("actionMicOff"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/res/Resources/Icons/Microphone_Red.ico"), QSize(), QIcon::Normal, QIcon::Off);
        actionMicOff->setIcon(icon3);
        actionPlay = new QAction(MainWindow);
        actionPlay->setObjectName(QString::fromUtf8("actionPlay"));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/res/Resources/Icons/Player Play_Green.ico"), QSize(), QIcon::Normal, QIcon::Off);
        actionPlay->setIcon(icon4);
        actionStop = new QAction(MainWindow);
        actionStop->setObjectName(QString::fromUtf8("actionStop"));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/res/Resources/Icons/Player Stop_Red.ico"), QSize(), QIcon::Normal, QIcon::Off);
        actionStop->setIcon(icon5);
        actionPause = new QAction(MainWindow);
        actionPause->setObjectName(QString::fromUtf8("actionPause"));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/res/Resources/Icons/Player Pause_Red.ico"), QSize(), QIcon::Normal, QIcon::Off);
        actionPause->setIcon(icon6);
        actionDebugTest1 = new QAction(MainWindow);
        actionDebugTest1->setObjectName(QString::fromUtf8("actionDebugTest1"));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/res/Resources/Icons/1.ico"), QSize(), QIcon::Normal, QIcon::Off);
        actionDebugTest1->setIcon(icon7);
        actionDebugTest2 = new QAction(MainWindow);
        actionDebugTest2->setObjectName(QString::fromUtf8("actionDebugTest2"));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/res/Resources/Icons/2.ico"), QSize(), QIcon::Normal, QIcon::Off);
        actionDebugTest2->setIcon(icon8);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout_3 = new QGridLayout(centralwidget);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        frame_2 = new QFrame(centralwidget);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(frame_2->sizePolicy().hasHeightForWidth());
        frame_2->setSizePolicy(sizePolicy1);
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        formLayout = new QFormLayout(frame_2);
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        formLayout->setContentsMargins(0, 0, 0, 0);

        gridLayout_3->addWidget(frame_2, 1, 0, 1, 1);

        frame = new QFrame(centralwidget);
        frame->setObjectName(QString::fromUtf8("frame"));
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(frame->sizePolicy().hasHeightForWidth());
        frame->setSizePolicy(sizePolicy2);
        frame->setAutoFillBackground(false);
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        frame->setLineWidth(0);
        gridLayout = new QGridLayout(frame);
        gridLayout->setSpacing(0);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        tabWidget = new QTabWidget(frame);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        QSizePolicy sizePolicy3(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(tabWidget->sizePolicy().hasHeightForWidth());
        tabWidget->setSizePolicy(sizePolicy3);
        tabWidget->setTabsClosable(false);
        tabMain = new QWidget();
        tabMain->setObjectName(QString::fromUtf8("tabMain"));
        gridLayout_2 = new QGridLayout(tabMain);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        frame_5 = new QFrame(tabMain);
        frame_5->setObjectName(QString::fromUtf8("frame_5"));
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Raised);
        gridLayout_4 = new QGridLayout(frame_5);
        gridLayout_4->setSpacing(0);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        gridLayout_4->setContentsMargins(0, 0, 0, 0);
        splitter = new QSplitter(frame_5);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setFrameShadow(QFrame::Raised);
        splitter->setLineWidth(5);
        splitter->setOrientation(Qt::Horizontal);
        splitter->setOpaqueResize(false);
        splitter->setHandleWidth(2);
        splitter->setChildrenCollapsible(true);
        frame_3 = new QFrame(splitter);
        frame_3->setObjectName(QString::fromUtf8("frame_3"));
        QSizePolicy sizePolicy4(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(frame_3->sizePolicy().hasHeightForWidth());
        frame_3->setSizePolicy(sizePolicy4);
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        gridLayout_5 = new QGridLayout(frame_3);
        gridLayout_5->setSpacing(0);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        gridLayout_5->setContentsMargins(0, 0, 0, 0);
        treeWidget1 = new QTreeWidget(frame_3);
        QTreeWidgetItem *__qtreewidgetitem = new QTreeWidgetItem();
        __qtreewidgetitem->setText(0, QString::fromUtf8("1"));
        treeWidget1->setHeaderItem(__qtreewidgetitem);
        treeWidget1->setObjectName(QString::fromUtf8("treeWidget1"));
        sizePolicy2.setHeightForWidth(treeWidget1->sizePolicy().hasHeightForWidth());
        treeWidget1->setSizePolicy(sizePolicy2);

        gridLayout_5->addWidget(treeWidget1, 0, 0, 1, 1);

        splitter->addWidget(frame_3);
        frame_4 = new QFrame(splitter);
        frame_4->setObjectName(QString::fromUtf8("frame_4"));
        QSizePolicy sizePolicy5(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy5.setHorizontalStretch(20);
        sizePolicy5.setVerticalStretch(0);
        sizePolicy5.setHeightForWidth(frame_4->sizePolicy().hasHeightForWidth());
        frame_4->setSizePolicy(sizePolicy5);
        frame_4->setFrameShape(QFrame::StyledPanel);
        frame_4->setFrameShadow(QFrame::Raised);
        gridLayout_6 = new QGridLayout(frame_4);
        gridLayout_6->setSpacing(0);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        gridLayout_6->setContentsMargins(0, 0, 0, 0);
        tableWidget1 = new QTableWidget(frame_4);
        if (tableWidget1->columnCount() < 7)
            tableWidget1->setColumnCount(7);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        tableWidget1->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        tableWidget1->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        tableWidget1->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        tableWidget1->setHorizontalHeaderItem(3, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        tableWidget1->setHorizontalHeaderItem(4, __qtablewidgetitem4);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        tableWidget1->setHorizontalHeaderItem(5, __qtablewidgetitem5);
        QTableWidgetItem *__qtablewidgetitem6 = new QTableWidgetItem();
        tableWidget1->setHorizontalHeaderItem(6, __qtablewidgetitem6);
        tableWidget1->setObjectName(QString::fromUtf8("tableWidget1"));
        sizePolicy3.setHeightForWidth(tableWidget1->sizePolicy().hasHeightForWidth());
        tableWidget1->setSizePolicy(sizePolicy3);
        tableWidget1->setAutoFillBackground(false);
        tableWidget1->horizontalHeader()->setVisible(true);
        tableWidget1->verticalHeader()->setVisible(false);

        gridLayout_6->addWidget(tableWidget1, 0, 0, 1, 1);

        splitter->addWidget(frame_4);

        gridLayout_4->addWidget(splitter, 0, 0, 1, 1);


        gridLayout_2->addWidget(frame_5, 0, 0, 1, 1);

        tabWidget->addTab(tabMain, QString());
        tabDebug = new QWidget();
        tabDebug->setObjectName(QString::fromUtf8("tabDebug"));
        gridLayout_7 = new QGridLayout(tabDebug);
        gridLayout_7->setObjectName(QString::fromUtf8("gridLayout_7"));
        frame_8 = new QFrame(tabDebug);
        frame_8->setObjectName(QString::fromUtf8("frame_8"));
        frame_8->setFrameShape(QFrame::StyledPanel);
        frame_8->setFrameShadow(QFrame::Raised);
        gridLayout_9 = new QGridLayout(frame_8);
        gridLayout_9->setObjectName(QString::fromUtf8("gridLayout_9"));
        frame_6 = new QFrame(frame_8);
        frame_6->setObjectName(QString::fromUtf8("frame_6"));
        sizePolicy4.setHeightForWidth(frame_6->sizePolicy().hasHeightForWidth());
        frame_6->setSizePolicy(sizePolicy4);
        frame_6->setFrameShape(QFrame::StyledPanel);
        frame_6->setFrameShadow(QFrame::Raised);
        gridLayout_10 = new QGridLayout(frame_6);
        gridLayout_10->setObjectName(QString::fromUtf8("gridLayout_10"));
        label1 = new QLabel(frame_6);
        label1->setObjectName(QString::fromUtf8("label1"));
        sizePolicy.setHeightForWidth(label1->sizePolicy().hasHeightForWidth());
        label1->setSizePolicy(sizePolicy);

        gridLayout_10->addWidget(label1, 0, 2, 1, 1);

        pushButton_2 = new QPushButton(frame_6);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        QSizePolicy sizePolicy6(QSizePolicy::Fixed, QSizePolicy::Preferred);
        sizePolicy6.setHorizontalStretch(0);
        sizePolicy6.setVerticalStretch(0);
        sizePolicy6.setHeightForWidth(pushButton_2->sizePolicy().hasHeightForWidth());
        pushButton_2->setSizePolicy(sizePolicy6);
        pushButton_2->setIcon(icon8);
        pushButton_2->setIconSize(QSize(32, 32));

        gridLayout_10->addWidget(pushButton_2, 0, 1, 1, 1);

        pushButtonAddRow = new QPushButton(frame_6);
        pushButtonAddRow->setObjectName(QString::fromUtf8("pushButtonAddRow"));
        QSizePolicy sizePolicy7(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy7.setHorizontalStretch(0);
        sizePolicy7.setVerticalStretch(0);
        sizePolicy7.setHeightForWidth(pushButtonAddRow->sizePolicy().hasHeightForWidth());
        pushButtonAddRow->setSizePolicy(sizePolicy7);
        pushButtonAddRow->setIcon(icon7);
        pushButtonAddRow->setIconSize(QSize(32, 32));

        gridLayout_10->addWidget(pushButtonAddRow, 0, 0, 1, 1);


        gridLayout_9->addWidget(frame_6, 0, 0, 1, 1);

        frame_7 = new QFrame(frame_8);
        frame_7->setObjectName(QString::fromUtf8("frame_7"));
        sizePolicy3.setHeightForWidth(frame_7->sizePolicy().hasHeightForWidth());
        frame_7->setSizePolicy(sizePolicy3);
        frame_7->setFrameShape(QFrame::StyledPanel);
        frame_7->setFrameShadow(QFrame::Raised);
        gridLayout_8 = new QGridLayout(frame_7);
        gridLayout_8->setObjectName(QString::fromUtf8("gridLayout_8"));
        textEditDebug1 = new QTextEdit(frame_7);
        textEditDebug1->setObjectName(QString::fromUtf8("textEditDebug1"));
        QFont font;
        font.setFamily(QString::fromUtf8("Courier New"));
        font.setPointSize(12);
        textEditDebug1->setFont(font);

        gridLayout_8->addWidget(textEditDebug1, 0, 0, 1, 1);


        gridLayout_9->addWidget(frame_7, 1, 0, 1, 1);


        gridLayout_7->addWidget(frame_8, 0, 0, 1, 1);

        tabWidget->addTab(tabDebug, QString());

        gridLayout->addWidget(tabWidget, 0, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer, 1, 0, 1, 1);


        gridLayout_3->addWidget(frame, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1044, 21));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        statusbar->setMouseTracking(false);
        MainWindow->setStatusBar(statusbar);
        toolBar = new QToolBar(MainWindow);
        toolBar->setObjectName(QString::fromUtf8("toolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, toolBar);

        menubar->addAction(menuFile->menuAction());
        menuFile->addAction(actionSettings);
        menuFile->addAction(actionExit);
        toolBar->addAction(actionExit);
        toolBar->addSeparator();
        toolBar->addAction(actionSettings);
        toolBar->addSeparator();
        toolBar->addAction(actionMicOn);
        toolBar->addAction(actionMicOff);
        toolBar->addAction(actionPlay);
        toolBar->addAction(actionPause);
        toolBar->addAction(actionStop);
        toolBar->addSeparator();
        toolBar->addAction(actionDebugTest1);
        toolBar->addAction(actionDebugTest2);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Art\304\261 Alt\304\261 VOIP Application V0.5", nullptr));
        actionExit->setText(QApplication::translate("MainWindow", "Exit", nullptr));
        actionSettings->setText(QApplication::translate("MainWindow", "Settings", nullptr));
        actionMicOn->setText(QApplication::translate("MainWindow", "Enable Microphone", nullptr));
#ifndef QT_NO_TOOLTIP
        actionMicOn->setToolTip(QApplication::translate("MainWindow", "Enable Microphone", nullptr));
#endif // QT_NO_TOOLTIP
        actionMicOff->setText(QApplication::translate("MainWindow", "Disable Microphone", nullptr));
        actionPlay->setText(QApplication::translate("MainWindow", "Play", nullptr));
#ifndef QT_NO_TOOLTIP
        actionPlay->setToolTip(QApplication::translate("MainWindow", "Play", nullptr));
#endif // QT_NO_TOOLTIP
        actionStop->setText(QApplication::translate("MainWindow", "Stop", nullptr));
#ifndef QT_NO_TOOLTIP
        actionStop->setToolTip(QApplication::translate("MainWindow", "Stop Play", nullptr));
#endif // QT_NO_TOOLTIP
        actionPause->setText(QApplication::translate("MainWindow", "Pause", nullptr));
#ifndef QT_NO_TOOLTIP
        actionPause->setToolTip(QApplication::translate("MainWindow", "Pause", nullptr));
#endif // QT_NO_TOOLTIP
        actionDebugTest1->setText(QApplication::translate("MainWindow", "Debug Test1", nullptr));
#ifndef QT_NO_TOOLTIP
        actionDebugTest1->setToolTip(QApplication::translate("MainWindow", "Debug Test1", nullptr));
#endif // QT_NO_TOOLTIP
        actionDebugTest2->setText(QApplication::translate("MainWindow", "Debug Test2", nullptr));
#ifndef QT_NO_TOOLTIP
        actionDebugTest2->setToolTip(QApplication::translate("MainWindow", "Debug Test2", nullptr));
#endif // QT_NO_TOOLTIP
        QTableWidgetItem *___qtablewidgetitem = tableWidget1->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("MainWindow", "Node Id", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = tableWidget1->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("MainWindow", "Node Description", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = tableWidget1->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QApplication::translate("MainWindow", "IP", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = tableWidget1->horizontalHeaderItem(3);
        ___qtablewidgetitem3->setText(QApplication::translate("MainWindow", "Location", nullptr));
        QTableWidgetItem *___qtablewidgetitem4 = tableWidget1->horizontalHeaderItem(4);
        ___qtablewidgetitem4->setText(QApplication::translate("MainWindow", "Connection", nullptr));
        QTableWidgetItem *___qtablewidgetitem5 = tableWidget1->horizontalHeaderItem(5);
        ___qtablewidgetitem5->setText(QApplication::translate("MainWindow", "Activity", nullptr));
        QTableWidgetItem *___qtablewidgetitem6 = tableWidget1->horizontalHeaderItem(6);
        ___qtablewidgetitem6->setText(QApplication::translate("MainWindow", "Registered", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tabMain), QApplication::translate("MainWindow", "Nodes", nullptr));
#ifndef QT_NO_TOOLTIP
        tabDebug->setToolTip(QApplication::translate("MainWindow", "Debug Tab", nullptr));
#endif // QT_NO_TOOLTIP
        label1->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        pushButton_2->setText(QString());
        pushButtonAddRow->setText(QString());
        tabWidget->setTabText(tabWidget->indexOf(tabDebug), QApplication::translate("MainWindow", "DEBUG", nullptr));
        menuFile->setTitle(QApplication::translate("MainWindow", "File", nullptr));
#ifndef QT_NO_TOOLTIP
        statusbar->setToolTip(QApplication::translate("MainWindow", "ddddddd", nullptr));
#endif // QT_NO_TOOLTIP
        toolBar->setWindowTitle(QApplication::translate("MainWindow", "toolBar", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
