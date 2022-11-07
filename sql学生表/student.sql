-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2022-11-02 17:17:33
-- 服务器版本： 5.7.26
-- PHP 版本： 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `student`
--

-- --------------------------------------------------------

--
-- 表的结构 `class`
--

CREATE TABLE `class` (
  `ClassNo` char(8) COLLATE utf8_unicode_ci NOT NULL,
  `DepartNo` char(2) COLLATE utf8_unicode_ci NOT NULL,
  `ClassName` char(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `class`
--

INSERT INTO `class` (`ClassNo`, `DepartNo`, `ClassName`) VALUES
('20040001', '01', '网络5041'),
('20040002', '01', '计算机5041'),
('20040003', '01', '计算机5042'),
('20040004', '04', '商务5041'),
('20040005', '04', '商务5042'),
('20040006', '02', '生技5041'),
('20040007', '03', '环资5041'),
('2005', '01', '网管3081'),
('20050001', '01', '计算机3051'),
('20050002', '01', '软件3051'),
('20050003', '02', '植保3051'),
('20050004', '03', '环资3051'),
('20050005', '04', '日语3051'),
('20060001', '01', '网络3061'),
('20060002', '01', '软件3061'),
('20070001', '01', '软件3071'),
('20050003', '02', '植保3051'),
('20050004', '03', '环资3051'),
('20050005', '04', '日语3051'),
('20060001', '01', '网络3061'),
('20060002', '01', '软件3061'),
('20070001', '01', '软件3071'),
('20070002', '05', '软件3072'),
('20050003', '02', '植保3051'),
('20050004', '03', '环资3051'),
('20050005', '04', '日语3051'),
('20060001', '01', '网络3061'),
('20060002', '01', '软件3061'),
('20070001', '01', '软件3071'),
('20070002', '05', '软件3072');

-- --------------------------------------------------------

--
-- 表的结构 `course`
--

CREATE TABLE `course` (
  `CouNo` char(3) COLLATE utf8_unicode_ci NOT NULL,
  `CouName` char(30) COLLATE utf8_unicode_ci NOT NULL,
  `Credit` decimal(3,1) NOT NULL,
  `Teacher` char(20) COLLATE utf8_unicode_ci NOT NULL,
  `DepartNo` char(2) COLLATE utf8_unicode_ci NOT NULL,
  `examkind` char(5) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `course`
--

INSERT INTO `course` (`CouNo`, `CouName`, `Credit`, `Teacher`, `DepartNo`, `examkind`) VALUES
('001', 'SQL Server数据库程序设计', '4.0', '张红霞', '01', '考试'),
('002', 'JAVA程序设计', '4.0', '王荣', '01', '考试'),
('003', '多媒体技术及应用', '2.0', '蒋晓华', '01', '考察'),
('004', '网络技术基础', '4.0', '杨华为', '01', '考试'),
('005', '网络安全与故障检测', '2.0', '朱建奇', '01', '考察'),
('006', '电子商务', '3.0', '陈云', '04', '考试'),
('007', '商务日语', '4.0', '李丽丽', '04', '考试'),
('008', '国际经济法', '2.0', '陆建军', '04', '考察'),
('009', '商务英语', '4.0', '钱月红', '04', '考试'),
('010', '环境监测', '4.0', '花海霞', '03', '考试'),
('011', '粮油品质检测', '2.0', '陈林', '03', '考察'),
('013', '网络数据库技术', '3.0', '程荣华', '01', '考查');

-- --------------------------------------------------------

--
-- 表的结构 `department`
--

CREATE TABLE `department` (
  `DepartNo` char(2) COLLATE utf8_unicode_ci NOT NULL,
  `DepartName` char(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `department`
--

INSERT INTO `department` (`DepartNo`, `DepartName`) VALUES
('01', '信息工程系'),
('02', '生物工程系'),
('03', '环境资源系'),
('04', '经贸系');

-- --------------------------------------------------------

--
-- 表的结构 `score`
--

CREATE TABLE `score` (
  `StuNo` char(10) COLLATE utf8_unicode_ci NOT NULL,
  `CouNo` char(3) COLLATE utf8_unicode_ci NOT NULL,
  `Score` decimal(5,1) NOT NULL,
  `category` char(5) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `score`
--

INSERT INTO `score` (`StuNo`, `CouNo`, `Score`, `category`) VALUES
('0463502101', '001', '85.0', '正考'),
('0463502101', '002', '89.5', '正考'),
('0463502101', '003', '91.0', '正考'),
('0463502101', '004', '78.0', '正考'),
('0463502102', '001', '68.0', '正考'),
('0463502102', '002', '60.0', '补考'),
('0463502102', '003', '72.0', '正考'),
('0463502102', '004', '61.0', '重修'),
('0463502103', '001', '78.5', '正考'),
('0463502103', '002', '80.0', '正考'),
('0463502103', '003', '83.0', '正考'),
('0463502103', '004', '69.0', '正考'),
('0463502104', '001', '94.0', '正考'),
('0463502104', '002', '92.0', '正考'),
('0463502104', '003', '87.0', '正考'),
('0463502104', '004', '89.0', '正考'),
('0463502105', '001', '62.0', '补考'),
('0463502105', '002', '67.0', '正考');

-- --------------------------------------------------------

--
-- 表的结构 `student`
--

CREATE TABLE `student` (
  `StuNo` char(10) COLLATE utf8_unicode_ci NOT NULL,
  `ClassNo` char(8) COLLATE utf8_unicode_ci NOT NULL,
  `StuName` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Birthdate` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `student`
--

INSERT INTO `student` (`StuNo`, `ClassNo`, `StuName`, `Birthdate`) VALUES
('0463501101', '20040002', '崔梅华', NULL),
('0463501102', '20040002', '葛一平  ', NULL),
('0463501103', '20040002', '钱莺莺  ', NULL),
('0463501104', '20040002', '卞海燕  ', NULL),
('0463501105', '20040002', '樊赛红  ', NULL),
('0463501106', '20040002', '郭晓庆  ', NULL),
('0463501107', '20040002', '万小青  ', NULL),
('0463501109', '20040002', '许晨光  ', NULL),
('0463501110', '20040002', '朱宏凯  ', NULL),
('0463501201', '20040003', '陈凯健  ', NULL),
('0463501202', '20040003', '蒋桂洋  ', NULL),
('0463501203', '20040003', '蔡晨燕  ', NULL),
('0463501204', '20040003', '李坚    ', NULL),
('0463501205', '20040003', '王锋锋  ', NULL),
('0463501206', '20040003', '崔永华  ', NULL),
('0463501207', '20040003', '钱艳玉  ', NULL),
('0463501208', '20040003', '史春飞  ', NULL),
('0463501209', '20040003', '夏小苛  ', NULL),
('0463501210', '20040003', '汪燕梅  ', NULL),
('0463502101', '20040001', '唐海燕  ', NULL),
('0463502102', '20040001', '施维维  ', NULL),
('0463502103', '20040001', '徐秋月  ', NULL),
('0463502104', '20040001', '钟宝妹  ', NULL),
('0463502105', '20040001', '倪滕龙  ', NULL),
('0463502106', '20040001', '陆勇    ', NULL),
('0463502107', '20040001', '姚小英  ', NULL),
('0463502108', '20040001', '崔子龙  ', NULL),
('0463502109', '20040001', '曹梅枫  ', NULL),
('0463502110', '20040001', '朱艳君  ', NULL);

-- --------------------------------------------------------

--
-- 表的结构 `teacher`
--

CREATE TABLE `teacher` (
  `teacherid` char(3) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `sex` char(2) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
