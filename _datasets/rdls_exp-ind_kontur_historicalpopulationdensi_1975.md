---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Human Settlement Layer (GHSL)
    url: https://data.humdata.org/dataset/india-historical-population-density-for-1975-2020-for-400m-h3-hexagons
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/india-historical-population-density-for-1975-2020-for-400m-h3-hexagons
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Kontur
  url: https://data.humdata.org/dataset/india-historical-population-density-for-1975-2020-for-400m-h3-hexagons
creator:
  affiliation: null
  email: null
  name: Kontur
  url: https://data.humdata.org/dataset/india-historical-population-density-for-1975-2020-for-400m-h3-hexagons
dataset_id: rdls_exp-ind_kontur_historicalpopulationdensi_1975
description: 'India population density for 1975 - 2020 for 400m H3 hexagons. Fixed
  up fusion of GHSL and OpenStreetMap data. Visit India: Population Density for 400m
  H3 Hexagons for up-to-date data.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/india-historical-population-density-for-1975-2020-for-400m-h3-hexagons]'
details: 'Historical population dataset of India in vector H3 hexagons was produced
  for data visualizations in an article on [India''s population growth](https://t.co/VRyTrwE54I).
  We thank Financial Times for their cooperation in making this dataset publicly available.
  **Dataset codebook**: **fid** [integer]: record order in data upload **h3** [h3index/text]:
  H3 index of hexagon **population** [double]: total population inside hexagon **geom**
  [geometry]: Polygon, EPSG:3857 **Up-to-date version of Kontur Population** is available
  at [https://data.humdata.org/organization/kontur](https://data.humdata.org/organization/kontur).
  Global Human Settlement Layer: Dataset: Schiavina, Marcello; Freire, Sergio; MacManus,
  Kytt (2019): GHS population grid multitemporal (1975, 1990, 2000, 2015) R2019A.
  European Commission, Joint Research Centre (JRC) DOI: 10.2905/42E8BE89-54FF-464E-BE7B-BF9E64DA5218
  PID: http://data.europa.eu/89h/0c6b9751-a71f-4062-830b-43c9f432370f Concept & Methodology:
  Freire, Sergio; MacManus, Kytt; Pesaresi, Martino; Doxsey-Whitfield, Erin; Mills,
  Jane (2016): Development of new open and free multi-temporal global population grids
  at 250 m resolution. Geospatial Data in a Changing World; Association of Geographic
  Information Laboratories in Europe (AGILE). AGILE 2016. OpenStreetMap: Some data
  (c) OpenStreetMap.org Contributors [Open Data Commons Open Database License](https://opendatacommons.org/licenses/odbl)
  (ODbL)'
exposure:
- asset_type:
    description: Historical gridded population density for India at 400m H3 hexagon
      resolution from 1975-2020
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
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Historical population density was derived from Global Human Settlement
    Layer satellite data and refined using OpenStreetMap reference data. Population
    counts were aggregated into H3 hexagonal grid cells at 400m resolution for India
    across ten time periods (1975-2020). The dataset provides baseline population
    exposure data for disaster risk assessment.
  sources:
  - id: source_1
    license: null
    name: Global Human Settlement Layer (GHSL)
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
- href: https://data.humdata.org/dataset/india-historical-population-density-for-1975-2020-for-400m-h3-hexagons
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
  url: https://h3geo.org
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://ghsl.jrc.ec.europa.eu
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons
    (Release 2023-06-22)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/historical_population_density/kontur_historical_population_density_for_2020_IN_20230621.gpkg
  format: null
  id: resource_d947785a
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_historical_population_density_for_2020_IN_20230621.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons
    (Release 2023-06-22)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/historical_population_density/kontur_historical_population_density_for_2015_IN_20230621.gpkg
  format: null
  id: resource_df0820b5
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_historical_population_density_for_2015_IN_20230621.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons
    (Release 2023-06-22)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/historical_population_density/kontur_historical_population_density_for_2010_IN_20230621.gpkg
  format: null
  id: resource_6a8287ed
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_historical_population_density_for_2010_IN_20230621.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons
    (Release 2023-06-22)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/historical_population_density/kontur_historical_population_density_for_2005_IN_20230621.gpkg
  format: null
  id: resource_17a40551
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_historical_population_density_for_2005_IN_20230621.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons
    (Release 2023-06-22)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/historical_population_density/kontur_historical_population_density_for_2000_IN_20230621.gpkg
  format: null
  id: resource_1e44d79c
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_historical_population_density_for_2000_IN_20230621.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons
    (Release 2023-06-22)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/historical_population_density/kontur_historical_population_density_for_1995_IN_20230621.gpkg
  format: null
  id: resource_f2b190a0
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_historical_population_density_for_1995_IN_20230621.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons
    (Release 2023-06-22)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/historical_population_density/kontur_historical_population_density_for_1990_IN_20230621.gpkg
  format: null
  id: resource_99a292b0
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_historical_population_density_for_1990_IN_20230621.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons
    (Release 2023-06-22)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/historical_population_density/kontur_historical_population_density_for_1985_IN_20230621.gpkg
  format: null
  id: resource_4b609ef1
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_historical_population_density_for_1985_IN_20230621.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons
    (Release 2023-06-22)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/historical_population_density/kontur_historical_population_density_for_1980_IN_20230621.gpkg
  format: null
  id: resource_6b1c8f65
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_historical_population_density_for_1980_IN_20230621.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons
    (Release 2023-06-22)'
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/historical_population_density/kontur_historical_population_density_for_1975_IN_20230621.gpkg
  format: null
  id: resource_f1ebf26b
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_historical_population_density_for_1975_IN_20230621.gpkg
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ind_kontur_historicalpopulationdensi_1975
spatial:
  bbox: null
  centroid: null
  countries:
  - IND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '1975-01-01'
temporal_resolution: null
title: 'India: Historical Population Density for 1975 - 2020 for 400m H3 Hexagons'
version: null
vulnerability: null
---
