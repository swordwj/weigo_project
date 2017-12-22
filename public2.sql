/*
 Navicat Premium Data Transfer

 Source Server         : localhost_5432
 Source Server Type    : PostgreSQL
 Source Server Version : 90605
 Source Host           : localhost:5432
 Source Catalog        : weigodb
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 90605
 File Encoding         : 65001

 Date: 27/11/2017 06:11:32
*/


-- ----------------------------
-- Sequence structure for admin_abmin_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."admin_abmin_id_seq";
CREATE SEQUENCE "public"."admin_abmin_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for comment_comment_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."comment_comment_id_seq";
CREATE SEQUENCE "public"."comment_comment_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for like_like_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."like_like_id_seq";
CREATE SEQUENCE "public"."like_like_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for message_message_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."message_message_id_seq";
CREATE SEQUENCE "public"."message_message_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for picture_picture_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."picture_picture_id_seq";
CREATE SEQUENCE "public"."picture_picture_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for relation_relation_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."relation_relation_id_seq";
CREATE SEQUENCE "public"."relation_relation_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for users_user_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."users_user_id_seq";
CREATE SEQUENCE "public"."users_user_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS "public"."admin";
CREATE TABLE "public"."admin" (
  "admin_id" int4 NOT NULL DEFAULT nextval('admin_abmin_id_seq'::regclass),
  "admin_name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL::character varying,
  "admin_password" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL::character varying
)
;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS "public"."comment";
CREATE TABLE "public"."comment" (
  "comment_id" int4 NOT NULL DEFAULT nextval('comment_comment_id_seq'::regclass),
  "comment_info" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL::character varying,
  "comment_time" timestamp(6) DEFAULT NULL::timestamp without time zone,
  "message_id" int4 NOT NULL DEFAULT NULL,
  "user_id" int4 NOT NULL DEFAULT NULL,
  "comm_commnum" int4 NOT NULL DEFAULT 0,
  "comm_likenum" int4 NOT NULL DEFAULT 0,
  "user_name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL::character varying
)
;

-- ----------------------------
-- Table structure for likes
-- ----------------------------
DROP TABLE IF EXISTS "public"."likes";
CREATE TABLE "public"."likes" (
  "like_id" int4 NOT NULL DEFAULT nextval('like_like_id_seq'::regclass),
  "message_id" int4 NOT NULL DEFAULT NULL,
  "user_id" int4 NOT NULL DEFAULT NULL
)
;

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS "public"."message";
CREATE TABLE "public"."message" (
  "message_id" int4 NOT NULL DEFAULT nextval('message_message_id_seq'::regclass),
  "message_info" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL::character varying,
  "message_time" timestamp(6) DEFAULT NULL::timestamp without time zone,
  "message_commentnum" int4 NOT NULL DEFAULT 1,
  "message_likenum" int4 NOT NULL DEFAULT 1,
  "message_transnum" int4 DEFAULT NULL,
  "user_id" int4 NOT NULL DEFAULT NULL
)
;

-- ----------------------------
-- Table structure for picture
-- ----------------------------
DROP TABLE IF EXISTS "public"."picture";
CREATE TABLE "public"."picture" (
  "picture_id" int4 NOT NULL DEFAULT nextval('picture_picture_id_seq'::regclass),
  "picture_url" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL::character varying,
  "picture_type" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "user_id" int4 NOT NULL DEFAULT NULL
)
;

-- ----------------------------
-- Table structure for relation
-- ----------------------------
DROP TABLE IF EXISTS "public"."relation";
CREATE TABLE "public"."relation" (
  "relation_id" int4 NOT NULL DEFAULT nextval('relation_relation_id_seq'::regclass),
  "user_id" int4 NOT NULL DEFAULT NULL,
  "follow_id" int4 NOT NULL DEFAULT NULL,
  "follow_name" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying
)
;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS "public"."users";
CREATE TABLE "public"."users" (
  "user_id" int4 NOT NULL DEFAULT nextval('users_user_id_seq'::regclass),
  "user_name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL::character varying,
  "user_password" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL::character varying,
  "follownum" int4 NOT NULL DEFAULT 0,
  "fansnum" int4 NOT NULL DEFAULT 0,
  "postnum" int4 NOT NULL DEFAULT 0,
  "userpic" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL
)
;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."admin_abmin_id_seq"
OWNED BY "public"."admin"."admin_id";
SELECT setval('"public"."admin_abmin_id_seq"', 3, false);
ALTER SEQUENCE "public"."comment_comment_id_seq"
OWNED BY "public"."comment"."comment_id";
SELECT setval('"public"."comment_comment_id_seq"', 36, true);
ALTER SEQUENCE "public"."like_like_id_seq"
OWNED BY "public"."likes"."like_id";
SELECT setval('"public"."like_like_id_seq"', 66, true);
ALTER SEQUENCE "public"."message_message_id_seq"
OWNED BY "public"."message"."message_id";
SELECT setval('"public"."message_message_id_seq"', 74, true);
ALTER SEQUENCE "public"."picture_picture_id_seq"
OWNED BY "public"."picture"."picture_id";
SELECT setval('"public"."picture_picture_id_seq"', 7, true);
ALTER SEQUENCE "public"."relation_relation_id_seq"
OWNED BY "public"."relation"."relation_id";
SELECT setval('"public"."relation_relation_id_seq"', 69, true);
ALTER SEQUENCE "public"."users_user_id_seq"
OWNED BY "public"."users"."user_id";
SELECT setval('"public"."users_user_id_seq"', 27, true);

-- ----------------------------
-- Primary Key structure for table admin
-- ----------------------------
ALTER TABLE "public"."admin" ADD CONSTRAINT "admin_pkey" PRIMARY KEY ("admin_id");

-- ----------------------------
-- Primary Key structure for table comment
-- ----------------------------
ALTER TABLE "public"."comment" ADD CONSTRAINT "comment_pkey" PRIMARY KEY ("comment_id");

-- ----------------------------
-- Primary Key structure for table likes
-- ----------------------------
ALTER TABLE "public"."likes" ADD CONSTRAINT "like_pkey" PRIMARY KEY ("like_id");

-- ----------------------------
-- Primary Key structure for table message
-- ----------------------------
ALTER TABLE "public"."message" ADD CONSTRAINT "message_pkey" PRIMARY KEY ("message_id");

-- ----------------------------
-- Primary Key structure for table picture
-- ----------------------------
ALTER TABLE "public"."picture" ADD CONSTRAINT "picture_pkey" PRIMARY KEY ("picture_id");

-- ----------------------------
-- Primary Key structure for table relation
-- ----------------------------
ALTER TABLE "public"."relation" ADD CONSTRAINT "relation_pkey" PRIMARY KEY ("relation_id");

-- ----------------------------
-- Primary Key structure for table users
-- ----------------------------
ALTER TABLE "public"."users" ADD CONSTRAINT "users_pkey" PRIMARY KEY ("user_id");
