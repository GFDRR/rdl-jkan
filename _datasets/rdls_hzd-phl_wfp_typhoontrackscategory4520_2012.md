---
attributions:
- entity:
    affiliation: null
    email: null
    name: Unisys Weather
    url: https://data.humdata.org/dataset/philippine-typhoon-tracks-category-4-and-5-from-2012-2016
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/philippine-typhoon-tracks-category-4-and-5-from-2012-2016
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/philippine-typhoon-tracks-category-4-and-5-from-2012-2016
dataset_id: rdls_hzd-phl_wfp_typhoontrackscategory4520_2012
description: 'A collection of the strongest typhoon (tracks and windspeed) data for
  the Philippines with category levels 4 and 5. Data were scrapped from http://weather.unisys.com/..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippine-typhoon-tracks-category-4-and-5-from-2012-2016]'
details: Please refer to http://weather.unisys.com/ for a detailed tracking information.
exposure: []
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Typhoon track and wind speed data were extracted from Unisys Weather
    satellite tracking records via web scraping. The dataset contains observed positions,
    wind speeds, and temporal information for Category 4-5 typhoons affecting the
    Philippines during 2012-2016, provided as point geometries (windspeed file) and
    polyline geometries (track path file).
  sources:
  - id: source_1
    license: null
    name: Unisys Weather
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippine-typhoon-tracks-category-4-and-5-from-2012-2016
  rel: source
loss:
  losses: []
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
  description: Philippines - Philippine Typhoon Tracks (Category 4 and 5) from 2012
    - 2016 (PH Typhoon tracks (windspeed) from 2012 to 2016 with category level 4
    and 5)
  download_url: https://data.humdata.org/dataset/3960d233-25f8-468b-8d0a-74499104a8b0/resource/ecc68be3-b7d3-44ee-aae8-3e5848bcbf36/download/ph_typhoon_tracks_windspeed_cat4_5_2012_2016.zip
  format: null
  id: resource_ecc68be3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PH_Typhoon_Tracks_windspeed_cat4_5_2012_2016.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Philippine Typhoon Tracks (Category 4 and 5) from 2012
    - 2016 (PH Typhoon tracks (path) from 2012 to 2016 with category level 4 and 5)
  download_url: https://data.humdata.org/dataset/3960d233-25f8-468b-8d0a-74499104a8b0/resource/59a314e8-98ac-4594-b2f4-f9230806393f/download/ph_typhoon_tracks_path_cat4_5_2012_2016.zip
  format: null
  id: resource_59a314e8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PH_Typhoon_Tracks_path_cat4_5_2012_2016.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_wfp_typhoontrackscategory4520_2012
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
  end: '2016-12-31'
  start: '2012-01-01'
temporal_resolution: null
title: Philippines - Philippine Typhoon Tracks (Category 4 and 5) from 2012 - 2016
version: null
vulnerability: null
---
