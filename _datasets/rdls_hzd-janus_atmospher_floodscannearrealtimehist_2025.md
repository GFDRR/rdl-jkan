---
attributions:
- entity:
    affiliation: null
    email: null
    name: Atmospheric and Environmental Research (AER) FloodScan
    url: https://data.humdata.org/dataset/floodscan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: JANUS Atmospheric and Environmental Research
  url: https://data.humdata.org/dataset/floodscan
creator:
  affiliation: null
  email: null
  name: JANUS Atmospheric and Environmental Research
  url: https://data.humdata.org/dataset/floodscan
dataset_id: rdls_hzd-janus_atmospher_floodscannearrealtimehist_2025
description: 'FloodScan uses satellite data to map and monitor floods daily, helping
  compare current flood conditions with historical averages. This dataset contains
  two resources: The first (hdx_floodscan_zonal_stats.xlsx) is a daily tabular dataset
  providing average FloodScan Standard Flood Extent Depiction (SFED) flood fraction
  (0-100%) per admin 1 and 2 level. Historical baseline values (SFED_BASELINE) are
  calculated per day-of-year from the last 10 years of historical data (non-inclusive
  of current year) after applying an 11 day smoothing mean window. Return Period (RP)
  is calculated empirically based on all historical data up to the current year (non-inclusive).
  The second resource (aer_floodscan_300s_SFED_90d.zip) is a zipped file containing
  AER FloodScan estimated daily flood fraction (0-100%) gridded data at approximately
  10 km resolution (300 arcseconds equivalent to approximately 0.083 degrees) for
  the last 90 days. Each file represents the estimates for a single day and includes
  2 bands: SFED and SFED_BASELINE. The baseline band provides users an easy way to
  compare current values with historical averages. The baseline is calculated per
  day-of-year from the last 10 years of historical data (non-inclusive of current
  year) after applying an 11 day temporal smoothing mean window.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/floodscan]'
details: Modified and Simplified by UN OCHA
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Daily SFED flood fraction rasters from AER satellite observations are
    smoothed with an 11-day centered rolling mean and aggregated to create day-of-year
    baseline climatology from 10 years of historical data (2013-2023). Return periods
    are calculated empirically by comparing current flood extent to this historical
    baseline. Data is provided as both gridded GeoTIFF rasters (300m resolution) and
    zonal statistics aggregated to administrative boundaries.
  sources:
  - id: source_1
    license: null
    name: Atmospheric and Environmental Research (AER) FloodScan
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/floodscan
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Daily Excel file containing date, admin metadata, raw SFED mean values
    (per admin 1 and 2), the approximate calculated return period and the baseline
    value calculated from the past 10 years of data.
  download_url: https://data.humdata.org/dataset/b704f489-6705-499a-b5f0-22eeb1184b0b/resource/b2108171-0a17-428f-9a28-7f3f7160d8f5/download/floodscan_readme.xlsx
  format: null
  id: resource_b2108171
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hdx_floodscan_zonal_stats.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Daily zip file containing previous 90 days of raster data with both
    SFED and SFED baseline bands.
  download_url: https://data.humdata.org/dataset/b704f489-6705-499a-b5f0-22eeb1184b0b/resource/7e76a4ae-57bd-40e0-acf9-a67def1e7f9b/download/baseline_zipped_file.zip
  format: null
  id: resource_7e76a4ae
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aer_floodscan_300s_SFED_90d.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-janus_atmospher_floodscannearrealtimehist_2025
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
  end: '2026-01-09'
  start: '2025-10-11'
temporal_resolution: null
title: 'FloodScan: Near Real-Time and Historical Flood Mapping'
version: null
vulnerability: null
---
