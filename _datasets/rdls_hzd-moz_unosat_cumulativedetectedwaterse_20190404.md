---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-extent-13-26-march-2019-over-sofala-province-mozambique
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-extent-13-26-march-2019-over-sofala-province-mozambique
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-extent-13-26-march-2019-over-sofala-province-mozambique
dataset_id: rdls_hzd-moz_unosat_cumulativedetectedwaterse_20190404
description: 'This map illustrates the cumulative satellite-detected surface waters
  in central provinces of Mozambique and particularly the Sofala province and its
  surroundings, as observed from the Sentinel-1 imagery acquired between 13 & 26 March
  2019. Within the analysis extent. over Sofala and Manica provinces, a total of 170,000
  km2 of surface imagery were analyzed and about 10,000 km2 of lands experienced floods
  within this period. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT. Satellite data : Sentinel-1
  Imagery date: 13-14-19-20-26 March 2019 Resolution: 10 m Copyright: Copernicus 2019/ESA
  Source:ESA Boundary data: OCHA ROSEA Water body & waterway: COD Analysis : UNITAR-UNOSAT
  Production:UNITAR - UNOSAT. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-extent-13-26-march-2019-over-sofala-province-mozambique]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-1 SAR imagery acquired over Sofala province between 13-26
    March 2019 was analyzed by UNOSAT analysts through multi-temporal change detection,
    comparing pre- and post-event images to delineate cumulative surface water extent.
    The resulting flood extent polygons were digitized and attributed with area measurements
    in hectares and square meters, representing observed inundation during the cyclone
    event.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-extent-13-26-march-2019-over-sofala-province-mozambique
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
  description: Cumulative Satellite detected waters extent overview between 13 & 26
    March 2019 over Sofala province, Mozambique (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/TC20190312MOZ/TC20190312MOZ_SHP.zip
  format: null
  id: resource_65c538f6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20190312MOZ_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cumulative Satellite detected waters extent overview between 13 & 26
    March 2019 over Sofala province, Mozambique (Geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/TC20190312MOZ/TC20190312MOZ.gdb.zip
  format: Geodatabase
  id: resource_4e88ddb4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20190312MOZ.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-moz_unosat_cumulativedetectedwaterse_20190404
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-04-04'
temporal_resolution: null
title: Cumulative Satellite detected waters extent overview between 13 & 26 March
  2019 over Sofala province, Mozambique
version: null
vulnerability: null
---
