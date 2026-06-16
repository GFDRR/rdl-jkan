---
attributions:
- entity:
    affiliation: null
    email: null
    name: 'Kontur Population: Global Population Density for 400m H3 Hexagons'
    url: https://data.humdata.org/dataset/kontur-boundaries-bahrain
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/kontur-boundaries-bahrain
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Kontur
  url: https://data.humdata.org/dataset/kontur-boundaries-bahrain
creator:
  affiliation: null
  email: null
  name: Kontur
  url: https://data.humdata.org/dataset/kontur-boundaries-bahrain
dataset_id: rdls_exp-bhr_kontur_bahrainadministrativedivi_20220407
description: 'Bahrain administrative division with aggregated population. Built from
  Kontur Population: Global Population Density for 400m H3 Hexagons on top of OpenStreetMap
  administrative boundaries data. Enriched with HASC codes for regions taken from
  Wikidata. Global version of boundaries dataset: Kontur Boundaries: Global administrative
  division with aggregated population. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/kontur-boundaries-bahrain]'
details: "**Dataset codebook (may be different for previous versions)**: **fid**:\
  \ (integer) record order in data upload. **admin_level**: (text) administrative\
  \ level of a feature based on government hierarchy in OSM. ''2'' is country level.\
  \ Higher levels may be adjusted according to region area to look more consistent\
  \ for different countries in the global version of the dataset. **osm_admin_level**:\
  \ (text) administrative level of a feature within a government hierarchy in OSM.\
  \ https://wiki.openstreetmap.org/wiki/Key:admin_level **name**: (text) primary name\
  \ of the feature in OSM https://wiki.openstreetmap.org/wiki/Key:name **name_en**:\
  \ (text) A common name in English language of the feature in OSM https://wiki.openstreetmap.org/wiki/Key:name:en\
  \ **population**: (double precision) total population of administrative boundary\
  \ based on aggregated population from Kontur Population: Global Population Density\
  \ for 400m H3 Hexagons dataset. **hasc**: (text) HASC and iso-3166-1 alpha-2 codes\
  \ of region taken from Wikidata by its connection with OSM feature using 'wikidata'\
  \ tag https://wiki.openstreetmap.org/wiki/Country_code, https://wiki.openstreetmap.org/wiki/Key:wikidata\
  \ **geom**: geometry (Polygon, EPSG 4326) Geometry representation of the data. **Global\
  \ version of Kontur Boundaries** is available at [https://data.humdata.org/organization/kontur](https://data.humdata.org/organization/kontur).\
  \ **Dataset codebook for topology build**: **fid**: (integer) record order in data\
  \ upload. **id**: (integer) record order in data upload. **admin_level**: (text)\
  \ administrative level of a feature based on government hierarchy in OSM. ''2''\
  \ is country level. Higher levels may be adjusted according to region area to look\
  \ more consistent for different countries in the global version of the dataset.\
  \ **maritime**: (boolean) flag which demonstrates if the border segment overlaps\
  \ with the maritime area. **Copyright** Wikidata. Hierarchical Administrative Subdivision\
  \ codes to represent country subdivisions is available under the [Creative Commons\
  \ CC0 License](https://creativecommons.org/publicdomain/zero/1.0/): [HASC - Wikidata](https://www.wikidata.org/wiki/Property:P8119)\
  \ Facebook High Resolution Settlement data: Facebook Connectivity Lab and Center\
  \ for International Earth Science Information Network - CIESIN - Columbia University.\
  \ 2016. High Resolution Settlement Layer (HRSL). Source imagery for HRSL \xC2\xA9\
  \ 2016 DigitalGlobe. Licence - Creative Commons Attribution International Global\
  \ Human Settlement Layer: Dataset: Schiavina, Marcello; Freire, Sergio; MacManus,\
  \ Kytt (2019): GHS population grid multitemporal (1975, 1990, 2000, 2015) R2019A.\
  \ European Commission, Joint Research Centre (JRC) DOI: 10.2905/42E8BE89-54FF-464E-BE7B-BF9E64DA5218\
  \ PID: [http://data.europa.eu/89h/0c6b9751-a71f-4062-830b-43c9f432370f](http://data.europa.eu/89h/0c6b9751-a71f-4062-830b-43c9f432370f)\
  \ Concept & Methodology: Freire, Sergio; MacManus, Kytt; Pesaresi, Martino; Doxsey-Whitfield,\
  \ Erin; Mills, Jane (2016): Development of new open and free multi-temporal global\
  \ population grids at 250 m resolution. Geospatial Data in a Changing World; Association\
  \ of Geographic Information Laboratories in Europe (AGILE). AGILE 2016. Copernicus\
  \ Global Land Service: Land Cover 100m: Marcel Buchhorn, Bruno Smets, Luc Bertels,\
  \ Bert De Roo, Myroslava Lesiv, Nandin-Erdene Tsendbazar, Martin Herold, Steffen\
  \ Fritz. (2020). Copernicus Global Land Service: Land Cover 100m: collection 3:\
  \ epoch 2019: Globe (Version V3.0.1) [Data set] licensed for reuse under [CC BY\
  \ 4.0](CC-BY-4.0). [Zenodo](http://doi.org/10.5281/zenodo.3939050).\
  \ Microsoft Buildings: (see the full list of locations in Methods). This data is\
  \ licensed by Microsoft under the Open Data Commons Open Database License (ODbL).\
  \ Land Information New Zealand (LINZ) NZ Building Outlines: sourced from the [LINZ\
  \ Data Service](https://data.linz.govt.nz/) licensed for reuse under [CC BY 4.0](CC-BY-4.0).\
  \ OpenStreetMap: Some data (c) OpenStreetMap.org Contributors [Open Data Commons\
  \ Open Database License](https://opendatacommons.org/licenses/odbl/) (ODbL)"
exposure:
- asset_type:
    description: Aggregated population counts at administrative division level derived
      from Kontur Population dataset
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Administrative boundaries were extracted from OpenStreetMap data using
    proprietary enhancements and filtered. Population counts were aggregated from
    the Kontur Population dataset (400m H3 hexagons) to administrative division level.
    Boundaries were enriched with HASC codes from Wikidata.
  sources:
  - id: source_1
    license: null
    name: 'Kontur Population: Global Population Density for 400m H3 Hexagons'
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kontur-boundaries-bahrain
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://data.humdata.org/m/dataset/kontur-population-dataset
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: Administrative Division with Aggregated Population (Release
    2022-04-07)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/kontur_boundaries_BH_20220407.gpkg.gz
  format: null
  id: resource_8d0cf797
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_boundaries_BH_20220407.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: Administrative Division with Aggregated Population (Release
    2023-06-28)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.amazonaws.com/kontur_datasets/kontur_boundaries_BH_20230628.gpkg.gz
  format: null
  id: resource_5ce06c36
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_boundaries_BH_20230628.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: Administrative Division with Aggregated Population (Release
    2023-06-28)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.amazonaws.com/kontur_datasets/kontur_topology_boundaries_BH_20230628.gpkg.gz
  format: null
  id: resource_2eb838b7
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_topology_boundaries_BH_20230628.gpkg
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bhr_kontur_bahrainadministrativedivi_20220407
spatial:
  bbox: null
  centroid: null
  countries:
  - BHR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-04-07'
temporal_resolution: null
title: 'Bahrain: Administrative Division with Aggregated Population'
version: null
vulnerability: null
---
