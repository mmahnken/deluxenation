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
-- Name: drawings_drawing; Type: TABLE; Schema: public; Owner: mmahnken; Tablespace: 
--

CREATE TABLE drawings_drawing (
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    title character varying(200) NOT NULL,
    id character varying(20) NOT NULL,
    favorite boolean NOT NULL,
    image character varying(100) NOT NULL,
    description text NOT NULL,
    notebook_id character varying(20) NOT NULL
);


ALTER TABLE drawings_drawing OWNER TO mmahnken;

--
-- Data for Name: drawings_drawing; Type: TABLE DATA; Schema: public; Owner: mmahnken
--

COPY drawings_drawing (created, modified, title, id, favorite, image, description, notebook_id) FROM stdin;
2016-09-03 13:09:48.509269-07	2016-09-03 15:50:17.624119-07	MDW	mdw	t	drawings/oriented.jpg	In flight drawing, MDW to OAK.	in-between-galaxies
2016-09-03 14:18:46.812138-07	2016-09-03 15:55:55.323769-07	Wavy Hair	wavy-hair	f	drawings/wavyh.JPG		in-between-galaxies
2016-09-03 13:11:02.115436-07	2016-09-03 15:56:13.470525-07	Vanity Williams	vanity-williams	f	drawings/vanitywill.JPG		in-between-galaxies
2016-09-03 13:12:55.963343-07	2016-09-03 15:56:34.373908-07	Toby Rustworthy	toby-rustworthy	f	drawings/jo.JPG		in-between-galaxies
2016-09-03 13:08:25.593389-07	2016-09-03 15:56:54.506275-07	Scurd	scurd	t	drawings/scurd.JPG		in-between-galaxies
2016-09-03 13:11:45.809085-07	2016-09-03 15:57:23.052332-07	Day After Pill	day-after-pill	f	drawings/morning.JPG		in-between-galaxies
2016-09-03 13:07:21.754494-07	2016-09-03 15:57:52.532417-07	Planet 6616	planet-6616	f	drawings/saturn2.JPG		in-between-galaxies
2016-09-03 12:57:24.474818-07	2016-09-03 16:01:50.729373-07	Rex Wattleigh	rex-wattleigh	t	drawings/rex.JPG		square-to-be-hip
2016-09-03 13:00:03.449286-07	2016-09-03 16:02:39.165184-07	Untitled	untitled-1	f	drawings/this.JPG		square-to-be-hip
2016-09-03 12:59:04.329703-07	2016-09-03 16:03:07.952983-07	Herminio Dulce	herminio-dulce	t	drawings/farmer.JPG	Mild-mannered farmer	square-to-be-hip
\.


--
-- Name: drawings_drawing_pkey; Type: CONSTRAINT; Schema: public; Owner: mmahnken; Tablespace: 
--

ALTER TABLE ONLY drawings_drawing
    ADD CONSTRAINT drawings_drawing_pkey PRIMARY KEY (id);


--
-- Name: drawings_drawing_03b31b8c; Type: INDEX; Schema: public; Owner: mmahnken; Tablespace: 
--

CREATE INDEX drawings_drawing_03b31b8c ON drawings_drawing USING btree (notebook_id);


--
-- Name: drawings_drawing_id_e1ad3179_like; Type: INDEX; Schema: public; Owner: mmahnken; Tablespace: 
--

CREATE INDEX drawings_drawing_id_e1ad3179_like ON drawings_drawing USING btree (id varchar_pattern_ops);


--
-- Name: drawings_drawing_notebook_id_a2eec757_like; Type: INDEX; Schema: public; Owner: mmahnken; Tablespace: 
--

CREATE INDEX drawings_drawing_notebook_id_a2eec757_like ON drawings_drawing USING btree (notebook_id varchar_pattern_ops);


--
-- Name: drawings_drawing_notebook_id_a2eec757_fk_drawings_notebook_id; Type: FK CONSTRAINT; Schema: public; Owner: mmahnken
--

ALTER TABLE ONLY drawings_drawing
    ADD CONSTRAINT drawings_drawing_notebook_id_a2eec757_fk_drawings_notebook_id FOREIGN KEY (notebook_id) REFERENCES drawings_notebook(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

