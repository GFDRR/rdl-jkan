---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Estellus
  url: https://lerma.obspm.fr/spip.php?article91&lang=fr
creator:
  affiliation: null
  email: null
  name: Estellus
  url: https://lerma.obspm.fr/spip.php?article91&lang=fr
dataset_id: rdls_hzd-crstac_globalinundationextentfrommultisatellitesgiems_giems3arcseconds
description: 'GIEMS at 3 arc seconds spatial resolution [Source: This metadata record
  was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://spdx.org/licenses/CC-BY-NC-SA-4.0.html
lineage:
  description: Provides maps of inundation percentage
  sources:
  - id: source_underlying_1
    license: null
    name: Multiple passive and active satellite instruments
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_2
    license: null
    name: 'e.g. AVHRR and SSM/I on-board ERS. Layers for downscaling: HydroSHEDS'
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_3
    license: null
    name: GLC2000
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_4
    license: null
    name: GLWD.
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Estellus
  url: https://lerma.obspm.fr/spip.php?article91&lang=fr
purpose: The datasets are available from author upon request, see webpage.
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1175/JHM-D-16-0155.1
  id: ref_doi
  name: null
  url: https://doi.org/10.1175/JHM-D-16-0155.1
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/flood/global-inundation-extent-from-multi-satellites-giems/giems-3-arc-seconds/giems-3-arc-seconds.json
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
  title: 'STAC Item: Global Inundation Extent from Multi-Satellites (GIEMS) - GIEMS
    3 arc seconds'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Inundation Extent from Multi-Satellites (GIEMS) - GIEMS 3 arc
    seconds - data file
  download_url: https://lerma.obspm.fr/spip.php?article91&lang=fr
  format: null
  id: resource_data-file_1
  media_type: format unknown
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Inundation Extent from Multi-Satellites (GIEMS) - GIEMS 3 arc seconds
    - data file
- access_url: https://doi.org/10.1175/JHM-D-16-0155.1
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Inundation Extent from Multi-Satellites (GIEMS) - GIEMS 3 arc
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
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_globalinundationextentfrommultisatellitesgiems_giems3arcseconds
spatial:
  bbox:
  - -180.0
  - -85.0
  - 180.0
  - 85.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 93
temporal:
  central_year: null
  duration: null
  end: '2007'
  start: '1993'
temporal_resolution: P1M
title: Global Inundation Extent from Multi-Satellites (GIEMS) - GIEMS 3 arc seconds
version: null
vulnerability: null
---
