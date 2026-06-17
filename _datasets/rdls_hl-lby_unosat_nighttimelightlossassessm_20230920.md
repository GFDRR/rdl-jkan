---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/night-time-light-loss-assessment-in-derna-al-bayda-libya-using-night-time-light-imagery
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/night-time-light-loss-assessment-in-derna-al-bayda-libya-using-night-time-light-imagery
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/night-time-light-loss-assessment-in-derna-al-bayda-libya-using-night-time-light-imagery
dataset_id: rdls_hl-lby_unosat_nighttimelightlossassessm_20230920
description: "UNOSAT code FL20230912LBY, GDACS Id: 1102204 Status: Significant light\
  \ loss observed. Further action(s): Continuous observations planned for full assessment\
  \ Severe floods in Libya have generated power supply outage in Derna and Al Bayd\u0101\
  . About 5 km2 in Derna, and 4 km2 in Al Bayd\u0101 became darker based on comparison\
  \ of SDGSAT-1 images acquired before and after the floods. River delta area in Derna\
  \ city lost the majority of night-time light, with power supply not fully restored\
  \ as of 17 September 2023. In Al Bayd\u0101, power supply has been almost fully\
  \ restored as of 17 September 2023. Continuous observations have been planned for\
  \ full assessment of power recovery.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/night-time-light-loss-assessment-in-derna-al-bayda-libya-using-night-time-light-imagery]"
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts compared SDGSAT-1 satellite imagery acquired before\
    \ and after the September 2023 floods in Libya to detect changes in night-time\
    \ light intensity. Areas showing significant light loss (5 km\xB2 in Derna, 4\
    \ km\xB2 in Al Bayda) were mapped as indicators of power supply disruption and\
    \ infrastructure damage from fluvial flooding."
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
- href: https://data.humdata.org/dataset/night-time-light-loss-assessment-in-derna-al-bayda-libya-using-night-time-light-imagery
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: "Power supply outage and night-time light loss affecting approximately\
      \ 5 km\xB2 in Derna and 4 km\xB2 in Al Bayda from fluvial flooding"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Night-Time Light Loss Assessment in Derna & Al Bayda (Libya) using
    Night-time Light Imagery (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3678/FL20230912LBY_gdb.zip
  format: Geodatabase
  id: resource_f58051b8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Night-Time Light Loss Assessment in Derna & Al Bayda (Libya) using
    Night-time Light Imagery (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3678/FL20230912LBY_SHP.zip
  format: null
  id: resource_f7be4f6a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-lby_unosat_nighttimelightlossassessm_20230920
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-20'
temporal_resolution: null
title: Night-Time Light Loss Assessment in Derna & Al Bayda (Libya) using Night-time
  Light Imagery
version: null
vulnerability: null
---
