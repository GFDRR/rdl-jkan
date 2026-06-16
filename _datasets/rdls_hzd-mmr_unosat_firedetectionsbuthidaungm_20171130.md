---
attributions:
- entity:
    affiliation: null
    email: null
    name: Moderate Resolution Imaging Spectroradiometer (MODIS)
    url: https://data.humdata.org/dataset/fire-detections-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2746
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Visible Infrared Imaging Radiometer Suite (VIIRS)
    url: https://data.humdata.org/dataset/fire-detections-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2746
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fire-detections-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2746
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fire-detections-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2746
dataset_id: rdls_hzd-mmr_unosat_firedetectionsbuthidaungm_20171130
description: 'This map illustrates areas of satellite detected fires in Buthindaung,
  Maungdaw, and Rathedaung Townships in the Maungdaw and Sittwe Districts of Rakhine
  State in Myanmar. Analysis used satellite- fire detections collected by the Moderate
  Resolution Imaging Spectroradiometer (MODIS) and the Visible Infrared Imaging Radiometer
  Suite (VIIRS) on multiple dates from 25 August to 25 November 2017. A total of 171
  fires were detected in different areas across Rathedaung, Buthindaung and Maungdaw
  townships during this period. While fire detections were spread out across the entire
  period analyzed, some notable clusters occurred on 28 August, 29 August, 3 September,
  15 September, 25 September, 9 October, and 6 November, as indicated in the map.
  Days of peak fire detection occurred on 28 August and 15 September as indicated
  in the chart. Note that due to cloud cover and satellite overpass times many fires
  occurring in the area during this period would not have been detected, and are generally
  only detected if the satellites are overhead while the fire is sufficiently active
  and clouds are not interfering. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/fire-detections-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2746]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
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
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Fire detections were identified from MODIS and VIIRS satellite thermal
    anomaly data collected between 25 August and 25 November 2017. UNOSAT analysts
    reviewed and validated satellite imagery to confirm fire locations across three
    townships in Rakhine State, resulting in 171 confirmed fire detections. The dataset
    represents observed wildfire events during the analysis period without probabilistic
    modeling or damage assessment.
  sources:
  - id: source_1
    license: null
    name: Moderate Resolution Imaging Spectroradiometer (MODIS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Visible Infrared Imaging Radiometer Suite (VIIRS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/fire-detections-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2746
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
  description: Fire Detections in Buthidaung, Maungdaw, and Rathedaung Townships of
    Rakhine State in Myanmar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/CE20130326MMR/Damage_Analysis_Rakhine_20171011.gdb.zip
  format: Geodatabase
  id: resource_f58b4af0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Damage_Analysis_Rakhine_20171011.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Fire Detections in Buthidaung, Maungdaw, and Rathedaung Townships of
    Rakhine State in Myanmar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/CE20130326MMR/Damage_Analysis_Rakhine_20171011_shp.zip
  format: null
  id: resource_d9fad9dc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Damage_Analysis_Rakhine_20171011_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mmr_unosat_firedetectionsbuthidaungm_20171130
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-30'
temporal_resolution: null
title: Fire Detections in Buthidaung, Maungdaw, and Rathedaung Townships of Rakhine
  State in Myanmar
version: null
vulnerability: null
---
