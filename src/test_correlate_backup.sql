--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 17.5

-- Started on 2025-07-11 12:14:30

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- TOC entry 215 (class 1259 OID 52099)
-- Name: gdp_by_county_state_year; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gdp_by_county_state_year (
    state text,
    county_state text,
    year text,
    gdp_in_thousand text
);


ALTER TABLE public.gdp_by_county_state_year OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 52114)
-- Name: gdp_by_county_state_year_summary; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gdp_by_county_state_year_summary (
    state text,
    year text,
    gdp_in_thousand double precision,
    gdp_in_thousand_scaled double precision
);


ALTER TABLE public.gdp_by_county_state_year_summary OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 52104)
-- Name: sales_by_county_state_year; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sales_by_county_state_year (
    product_type text,
    state text,
    county_state text,
    year text,
    sales_in_thousand text
);


ALTER TABLE public.sales_by_county_state_year OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 52109)
-- Name: sales_by_county_state_year_summary; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sales_by_county_state_year_summary (
    state text,
    year text,
    sales_in_thousand double precision,
    sales_in_thousand_scaled double precision
);


ALTER TABLE public.sales_by_county_state_year_summary OWNER TO postgres;

--
-- TOC entry 4842 (class 0 OID 52099)
-- Dependencies: 215
-- Data for Name: gdp_by_county_state_year; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gdp_by_county_state_year (state, county_state, year, gdp_in_thousand) FROM stdin;
CA	Los Angeles, CA	2023	756659481
IL	Cook, IL	2023	396470899
TX	Harris, TX	2023	357130669
NY	New York, NY	2023	343437442
AZ	Maricopa, AZ	2023	312350417
CA	Santa Clara, CA	2023	283522548
CA	Orange, CA	2023	278760587
WA	King, WA	2023	277642267
CA	San Diego, CA	2023	258725373
TX	Dallas, TX	2023	207533772
\.


--
-- TOC entry 4845 (class 0 OID 52114)
-- Dependencies: 218
-- Data for Name: gdp_by_county_state_year_summary; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gdp_by_county_state_year_summary (state, year, gdp_in_thousand, gdp_in_thousand_scaled) FROM stdin;
WA	2023	277642267	0
NY	2023	343437442	5.06
AZ	2023	312350417	2.67
IL	2023	396470899	9.14
CA	2023	1577667989	100
TX	2023	564664441	22.08
\.


--
-- TOC entry 4843 (class 0 OID 52104)
-- Dependencies: 216
-- Data for Name: sales_by_county_state_year; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sales_by_county_state_year (product_type, state, county_state, year, sales_in_thousand) FROM stdin;
laptop	CA	Los Angeles, CA	2023	200
laptop	IL	Cook, IL	2023	300
laptop	TX	Harris, TX	2023	500
laptop	NY	New York, NY	2023	600
laptop	AZ	Maricopa, AZ	2023	100
laptop	CA	Santa Clara, CA	2023	250
laptop	CA	Orange, CA	2023	600
laptop	WA	King, WA	2023	600
laptop	CA	San Diego, CA	2023	200
laptop	TX	Dallas, TX	2023	400
\.


--
-- TOC entry 4844 (class 0 OID 52109)
-- Dependencies: 217
-- Data for Name: sales_by_county_state_year_summary; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sales_by_county_state_year_summary (state, year, sales_in_thousand, sales_in_thousand_scaled) FROM stdin;
WA	2023	600	43.48
NY	2023	600	43.48
AZ	2023	100	0
IL	2023	300	17.39
CA	2023	1250	100
TX	2023	900	69.57
\.


-- Completed on 2025-07-11 12:14:30

--
-- PostgreSQL database dump complete
--

