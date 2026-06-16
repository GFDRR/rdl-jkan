---
attributions:
- entity:
    affiliation: null
    email: null
    name: ESA Copernicus Sentinel-1A
    url: https://data.humdata.org/dataset/tarlac-pampanga-pangasinan-standing-water-due-to-habagat-july-2018
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Google Earth Engine
    url: https://data.humdata.org/dataset/tarlac-pampanga-pangasinan-standing-water-due-to-habagat-july-2018
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/tarlac-pampanga-pangasinan-standing-water-due-to-habagat-july-2018
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/tarlac-pampanga-pangasinan-standing-water-due-to-habagat-july-2018
dataset_id: rdls_hzd-phl_wfp_tarlacpampangapangasinans_20180720
description: 'This is a standing water (possible inundated/flooded areas) in tarlac,
  pampanga and parts of pangasinan Philippines due to several typhoons and habagat
  (July 2018). Data were processed using Sentinel 1A GRD data (July 20, 2018) to map
  out areas with standing water . Thanks to ESA Copernicus program for the Sentinel
  1 data and Google for their cloud computing reource. This was processed in Google
  Earth Engine. For more detailed information, please contact michael.manalili@wfp.org
  or michaelandrew.manalili@gmail.com. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/tarlac-pampanga-pangasinan-standing-water-due-to-habagat-july-2018]'
details: Please contact the contributor for more detailed information
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
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Sentinel-1A GRD SAR data acquired on 20 July 2018 was processed in
    Google Earth Engine using image processing and cloud computing to detect standing
    water surfaces through backscatter analysis. The resulting raster map identifies
    inundated and flooded areas across Tarlac, Pampanga, and Pangasinan provinces
    following typhoon and habagat rainfall events.
  sources:
  - id: source_1
    license: null
    name: ESA Copernicus Sentinel-1A
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Google Earth Engine
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tarlac-pampanga-pangasinan-standing-water-due-to-habagat-july-2018
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
  description: This is a standing water (possible inundated/flooded areas) in tarlac,
    pampanga and parts of pangasinan Philippines due to several typhoons and habagat
    (July 2018)
  download_url: https://data.humdata.org/dataset/106693d0-98d9-4451-b506-83a6e03cb5e8/resource/2507184b-153c-4c4a-bacb-805a8a4179c2/download/standing_water_sentinel1_habagat_philippines_july202018.tif
  format: null
  id: resource_2507184b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: standing_water_Sentinel1_Habagat_Philippines_July202018.tif
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_wfp_tarlacpampangapangasinans_20180720
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-07-20'
temporal_resolution: null
title: Philippines - Tarlac, Pampanga, Pangasinan standing water due to habagat (July
  2018)
version: null
vulnerability: null
---
