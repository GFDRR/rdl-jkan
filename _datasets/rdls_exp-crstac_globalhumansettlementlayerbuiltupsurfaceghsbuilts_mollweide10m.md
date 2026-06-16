---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: JRC Data Catalogue
  url: https://human-settlement.emergency.copernicus.eu/ghs_buS2023.php
creator:
  affiliation: null
  email: null
  name: JRC Data Catalogue
  url: https://human-settlement.emergency.copernicus.eu/ghs_buS2023.php
dataset_id: rdls_exp-crstac_globalhumansettlementlayerbuiltupsurfaceghsbuilts_mollweide10m
description: 'GHS built-up surface grid, derived from Sentinel2 composite and Landsat,
  multitemporal (1975-2030) in Mollweide coordinates and 10 m spatial resolution.
  Residential (RES) or non residential (NRES) classifications are provided [Source:
  This metadata record was automatically extracted from the STAC catalog climate-risk-stac
  (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: urban/built-up footprints
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: CC-BY-4.0
lineage:
  description: GHS built-up surface spatial raster dataset, derived from Sentinel-2
    composite (2018) and Landsat, multitemporal (1975-2030)
  sources:
  - id: source_underlying_1
    license: null
    name: Sentinel2 composite and Landsat
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
  url: https://human-settlement.emergency.copernicus.eu/ghs_buS2023.php
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.2760/098587
  id: ref_doi
  name: null
  url: https://doi.org/10.2760/098587
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/global-human-settlement-layer-built-up-surface-ghs-built-s/mollweide-10-m/mollweide-10-m.json
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
  title: 'STAC Item: Global Human Settlement Layer - built-up surface (GHS-BUILT-S)
    - Mollweide 10 m'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:54009
  description: Global Human Settlement Layer - built-up surface (GHS-BUILT-S) - Mollweide
    10 m - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_BUILT_S_GLOBE_R2023A/GHS_BUILT_S_E2018_GLOBE_R2023A_54009_10/V1-0/GHS_BUILT_S_E2018_GLOBE_R2023A_54009_10_V1_0.zip
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - built-up surface (GHS-BUILT-S) - Mollweide
    10 m - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:54009
  description: Global Human Settlement Layer - built-up surface (GHS-BUILT-S) - Mollweide
    10 m - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_BUILT_S_GLOBE_R2023A/GHS_BUILT_S_NRES_E2018_GLOBE_R2023A_54009_10/V1-0/GHS_BUILT_S_NRES_E2018_GLOBE_R2023A_54009_10_V1_0.zip
  format: null
  id: resource_data-file_2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Human Settlement Layer - built-up surface (GHS-BUILT-S) - Mollweide
    10 m - data file
- access_url: https://doi.org/10.2760/098587
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Human Settlement Layer - built-up surface (GHS-BUILT-S) - Mollweide
    10 m (Web reference)
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
slug: rdls_exp-crstac_globalhumansettlementlayerbuiltupsurfaceghsbuilts_mollweide10m
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
spatial_resolution: 10
temporal:
  central_year: null
  duration: null
  end: '2018'
  start: '2018'
temporal_resolution: null
title: Global Human Settlement Layer - built-up surface (GHS-BUILT-S) - Mollweide
  10 m
version: null
vulnerability: null
---
