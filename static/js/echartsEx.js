$(function () {
    var myChart = echarts.init(document.getElementById('main'));
    myChart.showLoading();
    var data2 = {
        "name": "个人能力",
        "children": [
            {
                "name": "本职工作",
                "children": [
                    {"name": "软件测试",
                "children": [
                    {
                        "name": "静态测试",
                        "children": [
                            {
                                "name": "工具分析", "children": [
                                    {"name": "K9", "value": 2105},
                                    {"name": "QAC", "value": 2105},
                                    {"name": "TestBed", "value": 2105},
                                    {"name": "C++Test", "value": 2105},
                                ]
                            },
                            {
                                "name": "代码审查", "children": [
                                    {"name": "风格检查", "value": 2105},
                                    {"name": "注释检查", "value": 2105},
                                    {"name": "类定义检查", "value": 2105},
                                    {"name": "方法检查", "value": 2105},
                                    {"name": "循环检查", "value": 2105},
                                    {"name": "定义检查", "value": 2105},
                                    {"name": "IO检查", "value": 2105},
                                    {"name": "接口检查", "value": 2105},
                                    {"name": "其他检查", "value": 2105},
                                ]
                            },
                            {
                                "name": "文档审查", "children": [
                                    {"name": "完整性", "value": 2105},
                                    {"name": "一致性", "value": 2105},
                                    {"name": "准确性", "value": 2105},
                                ]
                            },
                            {
                                "name": "代码走查", "value": 2105
                            },
                        ]
                    },
                    {
                        "name": "动态测试",
                        "children": [
                            {"name": "功能测试", "value": 2105,},
                            {"name": "性能测试", "value": 2105,},
                            {"name": "接口测试", "value": 2105,},
                            {"name": "人机交互界面测试", "value": 2105,},
                            {"name": "强度测试", "value": 2105,},
                            {"name": "余量测试", "value": 2105,},
                            {"name": "可靠性测试", "value": 2105,},
                            {"name": "安全性测试", "value": 2105,},
                            {"name": "恢复性测试", "value": 2105,},
                            {"name": "边界测试", "value": 2105,},
                            {"name": "数据处理测试", "value": 2105,},
                            {"name": "安装性测试", "value": 2105,},
                            {"name": "容量测试", "value": 2105,},
                            {"name": "互操作性测试", "value": 2105,},
                            {"name": "敏感性测试", "value": 2105,},
                        ]
                    }
                ]
            },]},
            {
                "name": "项目",
                "children": [
                    {"name": "各种软件测试", "value": 2105},
                    {"name": "基于spin的软件并发问题的研究", "value": 1316},
                    {"name": "基于django某商品网站的开发", "value": 3151},
                    {"name": "文档自动生成工具的开发", "value": 3770},
                    {"name": "硬件集成电路安全性问题的检测", "value": 2435},
                    {"name": "硬件木马检测的研究", "value": 4839},
                    {"name": "个人博客网站的开发", "value": 1756},
                    {"name": "基于深度学习的图片分类的研究", "value": 4268},
                    {"name": "人工智能分类和回归问题算法的研究", "value": 1821},
                    {"name": "接口问题小工具开发（流产中）", "value": 5833}
                ]
            },
            {
                "name": "语言",
                "children": [
                    {"name": "C/C++", "value": 8833},
                    {"name": "python", "value": 8833},
                    {"name": "Verilog", "value": 8833},
                    {"name": "VHDL", "value": 8833},
                    {"name": "51汇编", "value": 8833},
                ]
            }
        ]
    };

    myChart.hideLoading();

    myChart.setOption(option = {
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove'
        },
        legend: {
            top: '2%',
            left: '3%',
            orient: 'vertical',
            data: [{
                name: 'tree1',
                icon: 'rectangle'
            },
                {
                    name: 'tree2',
                    icon: 'rectangle'
                }],
            borderColor: '#c23531'
        },
        series: [
            {
                type: 'tree',

                data: [data2],

                top: '1%',
                left: '10%',
                bottom: '1%',
                right: '20%',

                symbolSize: 10,

                label: {
                    position: 'left',
                    verticalAlign: 'middle',
                    align: 'right',
                    fontSize: 14
                },

                leaves: {
                    label: {
                        position: 'right',
                        verticalAlign: 'middle',
                        align: 'left'
                    }
                },

                expandAndCollapse: true,
                animationDuration: 550,
                animationDurationUpdate: 750
            }
        ]
    });


    myChart.setOption(option);
})