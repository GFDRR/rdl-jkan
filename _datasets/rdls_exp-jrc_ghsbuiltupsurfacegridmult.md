---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pesaresi M.
    url: https://human-settlement.emergency.copernicus.eu/ghs_buS2023.php
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
  url: https://data.jrc.ec.europa.eu/dataset/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea
creator:
  affiliation: null
  email: null
  name: EC Joint Research Centre
  url: https://human-settlement.emergency.copernicus.eu/ghs_buS2023.php
dataset_id: rdls_exp-jrc_ghsbuiltupsurfacegridmult
description: The spatial raster dataset depicts the distribution of the built-up (BU)
  surfaces estimates between 1975 and 2030 in 5 years intervals and two functional
  use components a) the total BU surface and b) the non-residential (NRES) BU surface.
  The data is made by spatial-temporal interpolation of five observed collections
  of multiple-sensor, multiple-platform satellite imageries. Landsat (MSS, TM, ETM
  sensor) supports the 1975, 1990, 2000, and 2014 epochs. Sentinel2 (S2) composite
  (GHS-composite-S2 R2020A) supports the 2018 epoch.
details: The built-up surface fraction (BUFRAC) is estimated at 10m of spatial resolution
  from the S2 image data, using as learning set a composite of data from GHS-BUILT-S2
  R2020A, Facebook, Microsoft, and Open Street Map (OSM) building delineation. The
  BUFRAC inference is made from the combination of quantized image features (reflectance,
  derivative of morphological profile DMP) through associative rule learning applied
  to spatial data analytics, which was introduced as symbolic machine learning (SML).
  The non-residential (NRES) domain is predicted from S2 image data by observation
  of radiometric, textural, and morphological features in an object-oriented image
  processing framework. The multi-temporal dimension is provided by testing by the
  SML the association between the combination of the quantized radiometric information
  collected by the Landsat imagery in the past epochs, and the "built-up" (BU) and
  "non-built-up" (NBU) class abstraction on image segments extracted from S2 images.
  The spatial-temporal interpolation is solved by rank-optimal spatial allocation
  using explanatory variables related to the landscape (slope, elevation, distance
  to water, and distance to vegetation) and related to the observed dynamic of BU
  surfaces in the past epochs.
exposure:
- asset_type: null
  category: buildings
  id: rdls_exp-jrc_ghsbuiltupsurfacegridmult_exp
  metrics:
  - dimension: structure
    id: rdls_exp-jrc_ghsbuiltupsurfacegridmult_m1
    measurement:
      quantity_kind: area
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
  - Martino Pesaresi
  date_published: '2023-01-01'
  doi: 10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA
  id: '0'
  name: GHS-POP R2023A - GHS population grid multitemporal (1975-2030)
  url: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea
- author_names:
  - Thomas Kemper
  date_published: '2023-01-01'
  doi: 10.2760/098587
  id: '1'
  name: GHSL Data Package 2023 report
  url: https://human-settlement.emergency.copernicus.eu/documents/GHSL_Data_Package_2023.pdf?t=1716923464
resources:
- access_url: https://human-settlement.emergency.copernicus.eu/download.php?ds=bu
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: ESRI:54009
  description: The spatial raster dataset depicts the distribution of built-up surfaces,
    expressed as number of square metres. The data report about the total built-up
    surface and the built-up surface allocated to dominant non-residential (NRES)
    uses. The product is available for different epochs, resolutions and coordinate
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
  title: GHS built-up surface (R2023)
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jrc_ghsbuiltupsurfacegridmult
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
title: GHS built-up surface grid multitemporal (1975-2030)
version: R2023
vulnerability: null
---
