---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: World Meteorological Organization WMO
  url: https://portal.grdc.bafg.de/applications/public.html?publicuser=PublicUser#dataDownload/Stations
creator:
  affiliation: null
  email: null
  name: World Meteorological Organization WMO
  url: https://portal.grdc.bafg.de/applications/public.html?publicuser=PublicUser#dataDownload/Stations
dataset_id: rdls_hzd-crstac_globalrunoffdatacentregrdc_riverdischargedata
description: 'River discharge from in-situ station globaly for 9500 stations. It provides
  daily, monthly, and long-term statistics [Source: This metadata record was automatically
  extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: deterministic
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
  event_sets_count: 1
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: River discharge from in-situ station globaly for 9500 stations. It
    provides daily, monthly, and long-term statistics
  sources: []
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: World Meteorological Organization WMO
  url: https://portal.grdc.bafg.de/applications/public.html?publicuser=PublicUser#dataDownload/Stations
purpose: null
referenced_by: []
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/flood/global-runoff-data-centre-grdc/river-discharge-data/river-discharge-data.json
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
  spatial_aggregation: station
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Global Runoff Data Centre (GRDC) - River Discharge Data'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Runoff Data Centre (GRDC) - River Discharge Data - data file
  download_url: https://portal.grdc.bafg.de/applications/public.html?publicuser=PublicUser#dataDownload/Stations
  format: null
  id: resource_data-file_1
  media_type: text/plain
  spatial: null
  spatial_aggregation: station
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Runoff Data Centre (GRDC) - River Discharge Data - data file
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_globalrunoffdatacentregrdc_riverdischargedata
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
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016'
  start: '1955'
temporal_resolution: P1D
title: Global Runoff Data Centre (GRDC) - River Discharge Data
version: null
vulnerability: null
---
