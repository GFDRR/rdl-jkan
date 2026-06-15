---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-north-gaza-governorate-damage-assessment-analysis-15-october-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-north-gaza-governorate-damage-assessment-analysis-15-october-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-north-gaza-governorate-damage-assessment-analysis-15-october-2023
dataset_id: rdls_el-pse_unosat_northgovernoratedamageass_20231018
description: 'UNOSAT code CE20231007PSE UNOSAT''s satellite imagery-based damage assessment
  detected damage and destruction to buildings within the area of interest in the
  North Gaza Governorate, Gaza Strip, based on an image collected on 15 October 2023
  when compared to images collected on 1 May 2023, 10 May 2023, and 18 September 2023.
  According to satellite imagery analysis, UNOSAT identified 927 destroyed structure,
  1216 severely damaged structures and 3121 moderately damaged structures, for a total
  of 5264 buildings. This corresponds to around 15% of the total structures in the
  North Gaza Governorate. One of the most affected area appears to be the one between
  Al Farata and Hai Abu Ghazala neighborhoods (inset 1). Among the affected structures,
  UNOSAT identified one school compound, namely the Beit Hanoun school, which eastern
  wing got severely damaged. Additionally, UNOSAT identified 271 affected road sections,
  either by impact craters or by debris. This is a preliminary analysis and has not
  yet been validated in the field.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-north-gaza-governorate-damage-assessment-analysis-15-october-2023]'
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
    description: Building stock in North Gaza Governorate classified by damage severity
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery from 15 October 2023 against
    baseline images from 1 May, 10 May, and 18 September 2023 to detect structural
    damage through visual change detection. Buildings were classified into three damage
    categories (destroyed, severely damaged, moderately damaged) based on observable
    changes in satellite imagery, producing a total count of 5,264 affected structures
    representing approximately 15% of the building stock in the study area.
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
- href: https://data.humdata.org/dataset/unosat-north-gaza-governorate-damage-assessment-analysis-15-october-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in North Gaza
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
  description: Palestine - UNOSAT North Gaza Governorate Damage Assessment Analysis
    - 15 October 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3693/UNOSAT_CE20231007PSE_Gaza_Governorate_DA_20231015_GDB.zip
  format: Geodatabase
  id: resource_90872330
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20231007PSE_Gaza_Governorate_DA_20231015_GDB.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_northgovernoratedamageass_20231018
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-18'
temporal_resolution: null
title: Palestine - UNOSAT North Gaza Governorate Damage Assessment Analysis - 15 October
  2023
version: null
vulnerability: null
---
