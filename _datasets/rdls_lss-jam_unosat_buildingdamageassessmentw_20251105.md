---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/building-damage-assessment-in-white-house-village-whitehouse-district-westmoreland-parishe
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-white-house-village-whitehouse-district-westmoreland-parishe
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-white-house-village-whitehouse-district-westmoreland-parishe
dataset_id: rdls_lss-jam_unosat_buildingdamageassessmentw_20251105
description: 'UNOSAT code: TC20251028JAM, GDACS ID: 1001230 This map illustrates the
  structures and buildings damaged by the passage of Hurricane MELISSA-25. The analysis
  focuses on White House Village in Westmoreland Parish, as of 31 October 2025. Damage
  and destruction were identified using very highresolution aerial imagery acquired
  by NOAA on 31 October 2025. In this area, UNOSAT identified a total of 1,875 affected
  buildings, of which 715 were completely destroyed and 1,160 were damaged. This is
  a preliminary analysis and has not yet been validated in the field. Ground verification
  is encouraged, and feedback can be sent to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/building-damage-assessment-in-white-house-village-whitehouse-district-westmoreland-parishe]'
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
  description: UNOSAT analysts reviewed very high-resolution NOAA aerial imagery acquired
    on 31 October 2025 and compared multi-temporal satellite images to identify structural
    damage caused by Hurricane MELISSA-25. Building-level damage classification (completely
    destroyed vs. damaged) was performed through visual interpretation of satellite
    imagery in White House Village, Westmoreland Parish, Jamaica, resulting in a preliminary
    damage inventory of 1,875 affected structures.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/building-damage-assessment-in-white-house-village-whitehouse-district-westmoreland-parishe
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Hurricane MELISSA-25 assessed via post-event
      satellite imagery
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
  - asset_category: buildings
    asset_dimension: structure
    description: Total affected buildings (damaged and destroyed) from Hurricane MELISSA-25
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Jamaica - Building Damage Assessment in White House Village, Whitehouse
    District, Westmoreland Parishe as of 31 October 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4215/TC20251028JAM_gdb.zip
  format: Geodatabase
  id: resource_6ab82c47
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20251028JAM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica - Building Damage Assessment in White House Village, Whitehouse
    District, Westmoreland Parishe as of 31 October 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4215/TC20251028JAM_SHP.zip
  format: null
  id: resource_6c2a081e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20251028JAM_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-jam_unosat_buildingdamageassessmentw_20251105
spatial:
  bbox: null
  centroid: null
  countries:
  - JAM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-11-05'
temporal_resolution: null
title: Jamaica - Building Damage Assessment in White House Village, Whitehouse District,
  Westmoreland Parishe as of 31 October 2025
version: null
vulnerability: null
---
