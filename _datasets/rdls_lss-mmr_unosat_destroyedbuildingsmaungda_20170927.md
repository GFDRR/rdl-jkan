---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/destroyed-buildings-in-maungdaw-and-buthindaung-townships-maungdaw-district-myanmar
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/destroyed-buildings-in-maungdaw-and-buthindaung-townships-maungdaw-district-myanmar
dataset_id: rdls_lss-mmr_unosat_destroyedbuildingsmaungda_20170927
description: 'This map illustrates satellite-detected destroyed or otherwise damaged
  structures in Maungdaw and Buthindaung townships, Maungdaw District, Myanmar. The
  analysis found a total area of more than 400 thousand square meters of destroyed
  structures occurring between 16 and 25 September 2017. This represents an increase
  of approximately 2% since last UNOSAT analysis with imagery collected on 16 September,
  when more than 20 square kilometers of destroyed structures were identified. Additionally,
  122 fires were detected within the area between 16 and 25 September 2017 by the
  MODIS and VIIRS sensors, with recent fire detections indicating destruction is likely
  ongoing. Most of the detected fires are located in the proximity of the affected
  areas as observed in the imagery collected 25 September. Finally, heavy cloud cover
  during the period in question, and on 16 and 25 September especially, indicates
  that destruction and fire detections are likely underestimated in this analysis.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/destroyed-buildings-in-maungdaw-and-buthindaung-townships-maungdaw-district-myanmar]'
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
  description: UNOSAT analysts compared satellite imagery from 16 and 25 September
    2017 to detect structural damage in Maungdaw and Buthindaung townships. Destroyed
    structures were identified through visual interpretation of satellite imagery
    changes, with additional fire detection from MODIS and VIIRS sensors. Results
    are provided as vector geodatabase and shapefile formats with damage polygons.
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
- href: https://data.humdata.org/dataset/destroyed-buildings-in-maungdaw-and-buthindaung-townships-maungdaw-district-myanmar
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
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Destroyed buildings in Maungdaw and Buthindaung townships, Maungdaw
    District, Myanmar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/CE20130326MMR/Damage_Analysis_Maungdaw_gdb.zip
  format: Geodatabase
  id: resource_37d2b492
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
  description: Destroyed buildings in Maungdaw and Buthindaung townships, Maungdaw
    District, Myanmar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/CE20130326MMR/Damage_Analysis_Maungdaw_shp.zip
  format: null
  id: resource_6bbbe61d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Damage_Analysis_Maungdaw_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mmr_unosat_destroyedbuildingsmaungda_20170927
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
  start: '2017-09-27'
temporal_resolution: null
title: Destroyed buildings in Maungdaw and Buthindaung townships, Maungdaw District,
  Myanmar
version: null
vulnerability: null
---
