--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: drawings_notebook; Type: TABLE; Schema: public; Owner: mmahnken; Tablespace: 
--

CREATE TABLE drawings_notebook (
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    id character varying(20) NOT NULL,
    title character varying(300) NOT NULL,
    description text NOT NULL,
    front_cover character varying(100) NOT NULL,
    back_cover character varying(100) NOT NULL,
    drawn_at date NOT NULL
);


ALTER TABLE drawings_notebook OWNER TO mmahnken;

--
-- Data for Name: drawings_notebook; Type: TABLE DATA; Schema: public; Owner: mmahnken
--

COPY drawings_notebook (created, modified, id, title, description, front_cover, back_cover, drawn_at) FROM stdin;
2016-09-03 13:06:07.00444-07	2016-09-03 14:59:11.350038-07	in-between-galaxies	In Between Galaxies		notebooks/frontcover.jpg	notebooks/IMG_2238.JPG	2016-06-01
2016-09-03 12:55:46.16559-07	2016-09-03 15:01:35.693547-07	square-to-be-hip	It's Square to be Hip	During a trip to Milwaukee, Wisconsin	notebooks/square-cover.JPG	notebooks/IMG_2236.JPG	2015-06-19
\.


--
-- Name: drawings_notebook_pkey; Type: CONSTRAINT; Schema: public; Owner: mmahnken; Tablespace: 
--

ALTER TABLE ONLY drawings_notebook
    ADD CONSTRAINT drawings_notebook_pkey PRIMARY KEY (id);


--
-- Name: drawings_notebook_id_f6e77aac_like; Type: INDEX; Schema: public; Owner: mmahnken; Tablespace: 
--

CREATE INDEX drawings_notebook_id_f6e77aac_like ON drawings_notebook USING btree (id varchar_pattern_ops);


--
-- PostgreSQL database dump complete
--

