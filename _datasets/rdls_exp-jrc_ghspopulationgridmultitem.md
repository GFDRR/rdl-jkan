---
attributions:
- entity:
    affiliation: null
    email: null
    name: Schiavina M.
    url: https://human-settlement.emergency.copernicus.eu/ghs_pop2023.php
  id: '0'
  role: author
- entity:
    affiliation: null
    email: null
    name: EC Joint Research Centre
    url: https://data.jrc.ec.europa.eu/dataset/2ff68a52-5b5b-4a22-8f40-c41da8332cfe
  id: '1'
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: jrc-ghsl-data@ec.europa.eu
  name: JRC GHSL
  url: https://data.jrc.ec.europa.eu/dataset/2ff68a52-5b5b-4a22-8f40-c41da8332cfe
creator:
  affiliation: null
  email: null
  name: EC Joint Research Centre
  url: https://human-settlement.emergency.copernicus.eu/ghs_pop2023.php
dataset_id: rdls_exp-jrc_ghspopulationgridmultitem
description: The spatial raster dataset depicts the distribution of residential population,
  expressed as the number of people per cell. Residential population estimates between
  1975 and 2020 in 5-year intervals and projections to 2025 and 2030 derived from
  CIESIN GPWv4.11 were disaggregated from census or administrative units to grid cells,
  informed by the distribution, volume, and classification of built-up as mapped in
  the Global Human Settlement Layer (GHSL) global layer per corresponding epoch.
details: 'This dataset is an update of the product released in 2022. Major improvements
  are the following: use of built-up volume maps (GHS-BUILT-V R2022A); use of more
  recent and detailed population estimates derived from GPWv4.11 integrating both
  UN World Population Prospects 2022 country population data and World Urbanisation
  Prospects 2018 data on Cities; revision of GPWv4.11 population growthrates by convergence
  to upper administrative level growthrates; systematic improvement of census coastlines;
  systematic revision of census units declared as unpopulated; integration of non-residential
  built-up volume information (GHS-BUILT-V_NRES R2023A); spatial resolution of 100m
  Mollweide (and 3 arcseconds in WGS84); projections to 2030.'
exposure:
- asset_type:
    description: null
    id: sei-pop
    scheme: GED4ALL
    title: null
    uri: null
  category: population
  id: rdls_exp-jrc_ghspopulationgridmultitem_exp
  metrics:
  - dimension: population
    id: rdls_exp-jrc_ghspopulationgridmultitem_m1
    measurement:
      quantity_kind: count
      unit: null
hazard: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: GHSL - Global Human Settlement Layer
  url: null
publisher:
  affiliation: null
  email: null
  name: JRC
  url: https://human-settlement.emergency.copernicus.eu/
purpose: null
referenced_by:
- author_names:
  - Marcello Schiavina
  - Sergio Freire
  - Alessandra Carioli
  - Kytt MacManus
  date_published: '2023-01-01'
  doi: 10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE
  id: '0'
  name: GHS-POP R2023A - GHS population grid multitemporal (1975-2030)
  url: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe
- author_names:
  - Thomas Kemper
  date_published: '2023-01-01'
  doi: 10.2760/098587
  id: '1'
  name: GHSL Data Package 2023 report
  url: https://human-settlement.emergency.copernicus.eu/documents/GHSL_Data_Package_2023.pdf?t=1716923464
resources:
- access_url: https://human-settlement.emergency.copernicus.eu/download.php?ds=pop
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: ESRI:54009
  description: The product is available for different epochs, resolutions and coordinate
    systems, but not all the combinations are available.
  download_url: null
  format: geotiff
  id: '0'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal:
    central_year: null
    duration: null
    end: '2030'
    start: '1975'
  temporal_resolution: P5Y
  title: GHS population grid (R2023)
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jrc_ghspopulationgridmultitem
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: GHS population grid multitemporal (1975-2030)
version: R2023
vulnerability: null
---
