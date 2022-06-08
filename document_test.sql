--
-- PostgreSQL database dump
--

-- Dumped from database version 13.6 (Ubuntu 13.6-0ubuntu0.21.10.1)
-- Dumped by pg_dump version 13.6 (Ubuntu 13.6-0ubuntu0.21.10.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Documents; Type: TABLE; Schema: public; Owner: nel
--

CREATE TABLE public."Documents" (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    text text NOT NULL,
    inserted_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);


ALTER TABLE public."Documents" OWNER TO nel;

--
-- Name: Documents_id_seq; Type: SEQUENCE; Schema: public; Owner: nel
--

CREATE SEQUENCE public."Documents_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Documents_id_seq" OWNER TO nel;

--
-- Name: Documents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nel
--

ALTER SEQUENCE public."Documents_id_seq" OWNED BY public."Documents".id;


--
-- Name: Rights; Type: TABLE; Schema: public; Owner: nel
--

CREATE TABLE public."Rights" (
    id integer NOT NULL,
    document_id integer NOT NULL,
    name character varying(255) NOT NULL,
    text text NOT NULL,
    rights_from timestamp with time zone NOT NULL,
    rights_to timestamp with time zone NOT NULL,
    inserted_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);


ALTER TABLE public."Rights" OWNER TO nel;

--
-- Name: Rights_id_seq; Type: SEQUENCE; Schema: public; Owner: nel
--

CREATE SEQUENCE public."Rights_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Rights_id_seq" OWNER TO nel;

--
-- Name: Rights_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nel
--

ALTER SEQUENCE public."Rights_id_seq" OWNED BY public."Rights".id;


--
-- Name: Documents id; Type: DEFAULT; Schema: public; Owner: nel
--

ALTER TABLE ONLY public."Documents" ALTER COLUMN id SET DEFAULT nextval('public."Documents_id_seq"'::regclass);


--
-- Name: Rights id; Type: DEFAULT; Schema: public; Owner: nel
--

ALTER TABLE ONLY public."Rights" ALTER COLUMN id SET DEFAULT nextval('public."Rights_id_seq"'::regclass);


--
-- Data for Name: Documents; Type: TABLE DATA; Schema: public; Owner: nel
--

COPY public."Documents" (id, name, text, inserted_at, updated_at) FROM stdin;
2	First document	That was the first document	2022-06-07 20:49:53.894909+03	2022-06-07 20:49:53.894909+03
4	Test document	Test Text	2022-06-07 22:09:45.753665+03	2022-06-07 22:09:45.753665+03
3	Test document!	Test Text	2022-06-07 22:03:28.345426+03	2022-06-07 22:09:45.783448+03
\.


--
-- Data for Name: Rights; Type: TABLE DATA; Schema: public; Owner: nel
--

COPY public."Rights" (id, document_id, name, text, rights_from, rights_to, inserted_at, updated_at) FROM stdin;
6	2	Test right!	That was the first right	2022-06-07 19:55:58+03	2022-06-07 19:56:45+03	2022-06-07 22:27:24.20206+03	2022-06-07 22:30:01.577568+03
17	2	Second right	That was the second right	2022-06-07 19:55:58+03	2022-06-07 19:56:45+03	2022-06-07 23:18:10.073895+03	2022-06-07 23:18:10.073895+03
\.


--
-- Name: Documents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nel
--

SELECT pg_catalog.setval('public."Documents_id_seq"', 24, true);


--
-- Name: Rights_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nel
--

SELECT pg_catalog.setval('public."Rights_id_seq"', 17, true);


--
-- Name: Documents Documents_pkey; Type: CONSTRAINT; Schema: public; Owner: nel
--

ALTER TABLE ONLY public."Documents"
    ADD CONSTRAINT "Documents_pkey" PRIMARY KEY (id);


--
-- Name: Rights Rights_pkey; Type: CONSTRAINT; Schema: public; Owner: nel
--

ALTER TABLE ONLY public."Rights"
    ADD CONSTRAINT "Rights_pkey" PRIMARY KEY (id);


--
-- Name: Rights Rights_document_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nel
--

ALTER TABLE ONLY public."Rights"
    ADD CONSTRAINT "Rights_document_id_fkey" FOREIGN KEY (document_id) REFERENCES public."Documents"(id);


--
-- PostgreSQL database dump complete
--

