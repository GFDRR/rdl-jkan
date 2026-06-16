---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/destroyed-buildings-in-maungdaw-and-buthindaung-townships-maungdaw-district-myanmar-2697
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/destroyed-buildings-in-maungdaw-and-buthindaung-townships-maungdaw-district-myanmar-2697
dataset_id: rdls_lss-mmr_unosat_updatedestroyedbuildingsm_20171005
description: 'This map illustrates satellite-detected destroyed or otherwise damaged
  structures in Maungdaw and Buthindaung townships, Maungdaw District, Myanmar. The
  analysis found a total area of more than 160 thousand square meters of destroyed
  structures occurring between 25 September and 1 October 2017. This represents an
  increase of approximately 1% since last UNOSAT analysis with imagery collected on
  25 September, when more than 20.5 square kilometers of destroyed structures were
  identified. Additionally, 6 fires were detected within the area between 25 September
  and 1 October 2017 by the MODIS and VIIRS sensors, with recent fire detections indicating
  destruction is likely ongoing. Most of the detected fires are located in the proximity
  of the affected areas as observed in the imagery collected 1 October. Finally, heavy
  cloud cover and haze during the period in question, indicates that destruction and
  fire detections are likely underestimated in this analysis. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/destroyed-buildings-in-maungdaw-and-buthindaung-townships-maungdaw-district-myanmar-2697]'
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery from 25 September
    and 1 October 2017 to detect structural damage in Maungdaw and Buthindaung townships.
    Damaged structures were digitized as polygons with area measurements in square
    meters and hectares, supplemented by MODIS fire detection data. The dataset represents
    post-event damage assessment from a complex emergency context.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/destroyed-buildings-in-maungdaw-and-buthindaung-townships-maungdaw-district-myanmar-2697
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction detected
      via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: 'Update: Destroyed buildings in Maungdaw and Buthindaung townships,
    Maungdaw District, Myanmar (Zipped geodatabase)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/CE20130326MMR/Damage_Analysis_Maungdaw_gdb.zip
  format: Geodatabase
  id: resource_1de96cc2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Damage_Analysis_Maungdaw_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Update: Destroyed buildings in Maungdaw and Buthindaung townships,
    Maungdaw District, Myanmar (Zipped shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/CE20130326MMR/Damage_Analysis_Maungdaw_shpb.zip
  format: null
  id: resource_8a5571de
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Damage_Analysis_Maungdaw_shpb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mmr_unosat_updatedestroyedbuildingsm_20171005
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
  start: '2017-10-05'
temporal_resolution: null
title: 'Update: Destroyed buildings in Maungdaw and Buthindaung townships, Maungdaw
  District, Myanmar'
version: null
vulnerability: null
---
