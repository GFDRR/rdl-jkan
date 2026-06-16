---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Human Settlement Layer (GHSL)
    url: https://data.humdata.org/dataset/kontur-population-dataset-22km
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Facebook High Resolution Settlement Layer (HRSL)
    url: https://data.humdata.org/dataset/kontur-population-dataset-22km
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Kontur
  url: https://data.humdata.org/dataset/kontur-population-dataset-22km
creator:
  affiliation: null
  email: null
  name: Kontur
  url: https://data.humdata.org/dataset/kontur-population-dataset-22km
dataset_id: rdls_exp-kontur_populationglobalpopulatio_2020
description: 'Global Population dataset. Vector H3 hexagons with population counts
  at 22km resolution. 400m resolution version: data.humdata.org/dataset/kontur-population-dataset
  3km resolution version: data.humdata.org/dataset/kontur-population-dataset-3km Per-country
  subsets of Kontur Population: data.humdata.org/organization/kontur Fixed up fusion
  of GHSL, Facebook, Microsoft Buildings, Copernicus Global Land Service Land Cover,
  Land Information New Zealand, and OpenStreetMap data.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/kontur-population-dataset-22km]'
details: "Dataset is primarily designed to support visualization behind https://disaster.ninja\
  \ project and may not be suitable for your specific needs. Please contact us if\
  \ you need custom processing or higher resolution version of this dataset. **Dataset\
  \ codebook**: **fid** [integer]: record order in data upload **h3** [h3index/text]:\
  \ H3 index of hexagon **population** [double]: total population inside hexagon **geom**\
  \ [geometry]: Polygon, EPSG:3857 **Global version of Kontur Population** is available\
  \ at [https://data.humdata.org/organization/kontur](https://data.humdata.org/organization/kontur).\
  \ Facebook High Resolution Settlement data: Facebook Connectivity Lab and Center\
  \ for International Earth Science Information Network - CIESIN - Columbia University.\
  \ 2016. High Resolution Settlement Layer (HRSL). Source imagery for HRSL \xC2\xA9\
  \ 2016 DigitalGlobe. Licence - Creative Commons Attribution International Global\
  \ Human Settlement Layer: Dataset: Schiavina M., Freire S., Carioli A., MacManus\
  \ K. (2023): GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European\
  \ Commission, Joint Research Centre (JRC) PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe,\
  \ doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE Concept & Methodology: Freire\
  \ S., MacManus K., Pesaresi M., Doxsey-Whitfield E., Mills J. (2016) Development\
  \ of new open and free multi-temporal global population grids at 250 m resolution.\
  \ Geospatial Data in a Changing World; Association of Geographic Information Laboratories\
  \ in Europe (AGILE), AGILE 2016. Copernicus Global Land Service: Land Cover 100m:\
  \ Marcel Buchhorn, Bruno Smets, Luc Bertels, Bert De Roo, Myroslava Lesiv, Nandin-Erdene\
  \ Tsendbazar, Martin Herold, Steffen Fritz. (2020). Copernicus Global Land Service:\
  \ Land Cover 100m: collection 3: epoch 2019: Globe (Version V3.0.1) [Data set].\
  \ Zenodo. http://doi.org/10.5281/zenodo.3939050 Microsoft Buildings: This data is\
  \ licensed by Microsoft under the [Open Data Commons Open Database License](https://opendatacommons.org/licenses/odbl)\
  \ (ODbL). Land Information New Zealand (LINZ) NZ Building Outlines: sourced from\
  \ the sourced from the [LINZ Data Service](https://data.linz.govt.nz) licensed for\
  \ reuse under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0). OpenStreetMap:\
  \ Some data (c) OpenStreetMap.org Contributors [Open Data Commons Open Database\
  \ License](https://opendatacommons.org/licenses/odbl) (ODbL) Geoalert Urban Mapping:\
  \ Chechnya, Moscow region, Tyva, Tashkent, Bukhara, Samarkand, Navoi, Chirchiq -\
  \ https://github.com/Geoalert/urban-mapping (ODbL). [World Population Prospects,\
  \ 2023 Revision](https://population.un.org/wpp/). United Nations Department of Economic\
  \ and Social Affairs, Population Division, Population Estimates and Projections\
  \ Section. 11 July 2022. Retrieved 10 February 2023."
exposure:
- asset_type:
    description: Global population counts aggregated into 22km H3 hexagonal grid cells
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
license: CC-BY-4.0
lineage:
  description: Global population counts were derived by fusing the Global Human Settlement
    Layer (GHSL) with Facebook's High Resolution Settlement Layer (HRSL) and aggregating
    results into H3 hexagonal grid cells at 22km resolution. The dataset provides
    baseline population exposure data without disaster-specific context.
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
    name: Facebook High Resolution Settlement Layer (HRSL)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kontur-population-dataset-22km
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
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://research.facebook.com/downloads/high-resolution-settlement-layer-hrsl
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 22km global hexagon population grid. Values represent number of people
    in cell. Release 2023-11-01.
  download_url: https://geodata-eu-central-1-kontur-public.s3.eu-central-1.amazonaws.com/kontur_datasets/kontur_population_20231101_r4.gpkg.gz
  format: null
  id: resource_b512f4b6
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_population_20231101_r4.gpkg.gz
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 22km global hexagon population grid. Values represent number of people
    in cell. Release 2022-06-30.
  download_url: https://data.humdata.org/dataset/9159a100-8672-4c5b-8162-c24459514bfa/resource/3f4ee676-1936-45e5-9a6a-aa224cf3aa39/download/kontur_population_20220630_r4.gpkg.gz
  format: null
  id: resource_3f4ee676
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kontur_population_20220630_r4.gpkg.gz
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-kontur_populationglobalpopulatio_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-11-01'
  start: '2020-03-11'
temporal_resolution: null
title: 'Kontur Population: Global Population Density for 22km H3 Hexagons'
version: null
vulnerability: null
---
