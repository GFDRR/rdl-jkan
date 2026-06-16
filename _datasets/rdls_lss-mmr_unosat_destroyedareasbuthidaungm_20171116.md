---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/destroyed-areas-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2727
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/destroyed-areas-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2727
dataset_id: rdls_lss-mmr_unosat_destroyedareasbuthidaungm_20171116
description: 'This map illustrates areas of satellite-detected destroyed or otherwise
  damaged settlements in Buthidaung, Maungdaw, and Rathedaung Townships in the Maungdaw
  and Sittwe Districts of Rakhine State in Myanmar. Analysis used satellite imagery
  collected on multiple dates between 31 August and 11 October 2017 and encompassed
  an area of about 4,800 square kilometers. Satellite analysis combined with information
  on settlement locations in Myanmar indicate that approximately 275 towns and villages
  were affected. This includes 34 in Buthidaung, 225 in Maungdaw, and 16 in Rathedaung.
  Note that these locations are indicated on the map though only a sampling are labeled
  due to the limitations of the map size and scale. Inset graphics show what is likely
  the village of Hpaw Ti Kaung, destroyed sometime between 16 September and 1 October
  2017, with only a few structures and trees undamaged. Continued cloud cover and
  haze during the period in question means that destruction is likely underestimated
  in this analysis. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/destroyed-areas-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2727]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery collected between
    31 August and 11 October 2017 across approximately 4,800 square kilometers in
    Rakhine State to identify notable changes in settlement structures. Damage assessments
    were conducted by visual interpretation of satellite imagery, identifying destroyed
    or damaged settlements and cross-referencing with settlement location databases
    to determine affected towns and villages.
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
- href: https://data.humdata.org/dataset/destroyed-areas-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2727
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected destroyed or damaged settlements in Rakhine State
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Destroyed areas in Buthidaung, Maungdaw, and Rathedaung Townships of
    Rakhine State in Myanmar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/CE20130326MMR/Damage_Analysis_Rakhine_20171011.gdb.zip
  format: Geodatabase
  id: resource_6e1e454c
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
  description: Destroyed areas in Buthidaung, Maungdaw, and Rathedaung Townships of
    Rakhine State in Myanmar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/CE20130326MMR/Damage_Analysis_Rakhine_20171011_shp.zip
  format: null
  id: resource_25a5cf2b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Damage_Analysis_Rakhine_20171011_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mmr_unosat_destroyedareasbuthidaungm_20171116
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
  start: '2017-11-16'
temporal_resolution: null
title: Destroyed areas in Buthidaung, Maungdaw, and Rathedaung Townships of Rakhine
  State in Myanmar
version: null
vulnerability: null
---
