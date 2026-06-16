---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: JRC Data Catalogue
  url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/
creator:
  affiliation: null
  email: null
  name: JRC Data Catalogue
  url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/
dataset_id: rdls_exp-crstac_globalhumansettlementlayerpopulationghspop_wgs8430arcseconds
description: 'GHS-POP in WGS84 coordinates and a spatial resolution of 30 arc seconds.
  Climate scenarios (as published): "extrapolation" [Source: This metadata record
  was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: population number
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
  description: The Global Human Settlement Layer Population (GHS-POP) datasets are
    available in two different coordinate systems and two spatial resolutions each
    for the years 1975-2030 in 5-year time intervals.
  sources:
  - id: source_underlying_1
    license: null
    name: Gridded Population of the World (GPW) v4
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_2
    license: null
    name: GHS built-up land (GHS-BUILT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: JRC Data Catalogue
  url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/
purpose: GHS-POP may underestimate population in sparsely populated locations where
  settlements are not detected by the satellite; it may therefore overconcentrate
  population in those locations where settlements are detected.
referenced_by:
- author_names: null
  date_published: null
  doi: 10.2760/098587
  id: ref_doi
  name: null
  url: https://doi.org/10.2760/098587
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/population/global-human-settlement-layer-population-ghs-pop/wgs84-30-arc-seconds/wgs84-30-arc-seconds.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Global Human Settlement Layer - population (GHS-POP) - WGS84
    30 arc seconds'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E1975_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E1975_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E1980_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E1980_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E1985_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E1985_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E1990_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E1990_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E1995_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E1995_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E2000_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E2000_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E2005_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E2005_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E2010_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E2010_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E2015_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E2015_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E2020_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E2020_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_10
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E2025_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E2025_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_11
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E2030_GLOBE_R2023A_4326_30ss/V1-0/GHS_POP_E2030_GLOBE_R2023A_4326_30ss_V1_0.zip
  format: null
  id: resource_data-file_12
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
    - data file
- access_url: https://doi.org/10.2760/098587
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc
    seconds (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_globalhumansettlementlayerpopulationghspop_wgs8430arcseconds
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 926
temporal:
  central_year: null
  duration: null
  end: '2030'
  start: '1975'
temporal_resolution: P5Y
title: Global Human Settlement Layer - population (GHS-POP) - WGS84 30 arc seconds
version: null
vulnerability: null
---
