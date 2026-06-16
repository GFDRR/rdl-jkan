---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/power-supply-assessment-in-benghazi-libya-using-night-time-light-imagery
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/power-supply-assessment-in-benghazi-libya-using-night-time-light-imagery
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/power-supply-assessment-in-benghazi-libya-using-night-time-light-imagery
dataset_id: rdls_hel-lby_unosat_powersupplyassessmentbeng_20230927
description: 'UNOSAT code FL20230912LBY, GDACS Id: 1102204 Status: Power outage observed.
  Further action(s): continue monitoring Compared with Derna and Al Bayda, power supply
  of Benghazi was less affected by the floods. No significant power outage could be
  observed in Benghazi. Only a few areas east of the city of Benghazi suffered of
  power outage after the floods, in which the power supply has recovered to pre-floods
  level on 24 September 2023.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/power-supply-assessment-in-benghazi-libya-using-night-time-light-imagery]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Power supply infrastructure and electrical grid assets in Benghazi
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (night-time
    light imagery) acquired before and after the September 2023 floods in Libya to
    detect changes in power supply infrastructure functionality. The analysis identified
    areas of power outage in Benghazi and tracked recovery to pre-flood levels by
    24 September 2023, producing vector geodatabase and shapefile outputs with confidence
    and validation fields.
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
- href: https://data.humdata.org/dataset/power-supply-assessment-in-benghazi-libya-using-night-time-light-imagery
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct power outage impact from fluvial flooding in Benghazi, with
      recovery timeline documented
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Power Supply Assessment in Benghazi (Libya) using Night-time Light
    Imagery (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3680/FL20230912LBY_gdb.zip
  format: Geodatabase
  id: resource_0b3464f7
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
  description: Power Supply Assessment in Benghazi (Libya) using Night-time Light
    Imagery (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3680/FL20230912LBY_SHP.zip
  format: null
  id: resource_a9b15585
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-lby_unosat_powersupplyassessmentbeng_20230927
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
  start: '2023-09-27'
temporal_resolution: null
title: Power Supply Assessment in Benghazi (Libya) using Night-time Light Imagery
version: null
vulnerability: null
---
