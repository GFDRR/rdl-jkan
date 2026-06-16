---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNITAR - UNOSAT
    url: https://data.humdata.org/dataset/damage-density-2016-of-hama-hama-governorate-syria
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: REACH Initiative
    url: https://data.humdata.org/dataset/damage-density-2016-of-hama-hama-governorate-syria
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-2016-of-hama-hama-governorate-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-2016-of-hama-hama-governorate-syria
dataset_id: rdls_lss-syr_unosat_2016damagedensityhamahama_20170117
description: 'This map illustrates satellite-detected damage density in the city of
  Hama, Hama Governorate, Syria. Using satellite imagery acquired 06 July and 30 June
  2016, 05 March 2014, 26 September 2013, and 06 August 2010, UNITAR - UNOSAT identified
  a total of 5,968 affected structures, of which 4,969 were destroyed, 345 severely
  damaged, and 654 moderately damaged. This analysis does not include pre-war military
  bases and facilities. This analysis was done as part of the REACH initiative for
  the U.S. Office of Foreign Disaster Assistance. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR -
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-density-2016-of-hama-hama-governorate-syria]'
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
  description: Multi-temporal satellite imagery from 2010, 2013, 2014, and 2016 was
    analyzed by UNOSAT analysts to detect and classify structural damage in Hama city,
    Syria, resulting from conflict. Analysts compared imagery pairs to identify destroyed,
    severely damaged, and moderately damaged structures, excluding pre-war military
    facilities. The output is a georeferenced vector dataset of affected structures
    classified by damage severity.
  sources:
  - id: source_1
    license: null
    name: UNITAR - UNOSAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-density-2016-of-hama-hama-governorate-syria
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected building damage in Hama city from conflict, with
      4,969 destroyed, 345 severely damaged, and 654 moderately damaged structures
      identified via multi-date imagery analysis
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
  description: Syria - 2016 Damage density in Hama, Hama Governorate (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
  format: Geodatabase
  id: resource_5eec0915
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Syria - 2016 Damage density in Hama, Hama Governorate (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_shp.zip
  format: null
  id: resource_998f19ab
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_unosat_2016damagedensityhamahama_20170117
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-01-17'
temporal_resolution: null
title: Syria - 2016 Damage density in Hama, Hama Governorate
version: null
vulnerability: null
---
