---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA MODIS Aqua/Terra satellite
    url: https://data.humdata.org/dataset/geodata-of-snow-cover-extent-over-west-bank-israel-jordan-lebanon-and-syria-january-13-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-snow-cover-extent-over-west-bank-israel-jordan-lebanon-and-syria-january-13-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-snow-cover-extent-over-west-bank-israel-jordan-lebanon-and-syria-january-13-2015
dataset_id: rdls_hzd-isrjorlbnpsesyr_unosat_geodatasnowcoverextentove_20150113
description: 'This map illustrates the extent of the snow cover caused by the storm
  ''Huda'' that moved through the Middle East region striking Lebanon, Jordan, and
  the West Bank from about 7-13 January. This analysis was based on satellite imagery
  collected by the MODIS sensor on the NASA AQUA satellite on 13 January 2015. As
  seen in the imagery the snow has covered a very extensive part of the Lebanon and
  Syria. A decrease in the snow cover extent is observed in certain areas in Southern
  Lebanon and Syria compared to previous UNOSAT analysis with imagery collected on
  12 January. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-snow-cover-extent-over-west-bank-israel-jordan-lebanon-and-syria-january-13-2015]'
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
        process: extratropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts interpreted MODIS satellite imagery collected on 13
    January 2015 to delineate snow cover extent across the Levant region following
    extratropical cyclone 'Huda'. Multi-temporal comparison with 12 January imagery
    identified changes in snow cover distribution. The resulting vector dataset represents
    the observed spatial extent of snow cover as a proxy for the cyclone's impact
    footprint.
  sources:
  - id: source_1
    license: null
    name: NASA MODIS Aqua/Terra satellite
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-snow-cover-extent-over-west-bank-israel-jordan-lebanon-and-syria-january-13-2015
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
  description: Geodata of Snow cover extent over West Bank, Israel, Jordan, Lebanon
    and Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/PS/ST20150107PSE/Modis_Aqua_Terra_Snowcover_20150113.zip
  format: null
  id: resource_e483e55a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Modis_Aqua_Terra_Snowcover_20150113.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-isrjorlbnpsesyr_unosat_geodatasnowcoverextentove_20150113
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  - ISR
  - JOR
  - LBN
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-01-13'
temporal_resolution: null
title: Geodata of Snow cover extent over West Bank, Israel, Jordan, Lebanon and Syria
version: null
vulnerability: null
---
