---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: JRC
  url: https://global-flood.emergency.copernicus.eu/general-information/data-and-services/
creator:
  affiliation: null
  email: null
  name: JRC
  url: https://global-flood.emergency.copernicus.eu/general-information/data-and-services/
dataset_id: rdls_hzd-crstac_glofasglobalfloodmonitoringglofasgfm_observedwaterextent
description: 'All pixels classified as open and calm water using Sentinel-1 SAR backscatter
  intensity [Source: This metadata record was automatically extracted from the STAC
  catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: observed
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
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: A continuous monitoring of floods worldwide by immediately processing
    and analyzing all incoming Copernicus Sentinel-1 Synthetic Aperture Radar (SAR)
    satellite data
  sources:
  - id: source_underlying_1
    license: null
    name: Sentinel-1 SAR
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
  name: JRC
  url: https://global-flood.emergency.copernicus.eu/general-information/data-and-services/
purpose: user account needed for data download
referenced_by: []
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/flood/glofas-global-flood-monitoring-glofas-gfm/observed-water-extent/observed-water-extent.json
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
  title: 'STAC Item: GloFAS Global Flood Monitoring (GloFAS-GFM) - Observed water
    Extent'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: GloFAS Global Flood Monitoring (GloFAS-GFM) - Observed water Extent
    - data file
  download_url: https://global-flood.emergency.copernicus.eu/general-information/data-and-services/
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GloFAS Global Flood Monitoring (GloFAS-GFM) - Observed water Extent - data
    file
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_glofasglobalfloodmonitoringglofasgfm_observedwaterextent
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
  end: '2026'
  start: '2015'
temporal_resolution: null
title: GloFAS Global Flood Monitoring (GloFAS-GFM) - Observed water Extent
version: null
vulnerability: null
---
