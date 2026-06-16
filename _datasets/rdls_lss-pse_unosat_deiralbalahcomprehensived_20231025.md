---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-deir-al-balah-comprehensive-damage-assessment-gaza-strip-21-october-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-deir-al-balah-comprehensive-damage-assessment-gaza-strip-21-october-2023
dataset_id: rdls_lss-pse_unosat_deiralbalahcomprehensived_20231025
description: 'UNOSAT code CE20231007PSE UNOSAT conducted a satellite-imagery based
  comprehensive damage assessment to detected damage and destruction to structures
  within the area of interest in the Deir Al-Balah Governorate, Gaza Strip, using
  an image collected on 21 October 2023 and compared it to an image collected on 15
  October 2023. According to the satellite imagery analysis, UNOSAT identified a total
  of 197 destroyed structures, 143 severely damaged structures, and 435 moderately
  damaged structures, for a total of 775 affected structures as of 21 October 2023.
  This corresponds to less than 2% of the total structures in the Deir Al-Balah Governorate.
  The most affected area appears to be the Al Bureij Camp neighborhood, where the
  number of damaged structures per square kilometer is the highest, followed by the
  Al Awda neighborhood. Among the newly affected structures, UNOSAT identified a mosque,
  namely the Al-Salam Mosque, visibly destroyed. Additionally, UNOSAT identified 42
  affected road sections, either by impact craters or by debris. This is a preliminary
  analysis and has not yet been validated in the field.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/unosat-deir-al-balah-comprehensive-damage-assessment-gaza-strip-21-october-2023]'
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
  description: UNOSAT analysts conducted multi-temporal satellite imagery analysis
    comparing images from 15 October 2023 and 21 October 2023 to detect and classify
    structural damage in Deir Al-Balah. Damage was categorized into three severity
    classes (destroyed, severely damaged, moderately damaged) through visual interpretation
    of satellite imagery, resulting in a comprehensive post-event damage inventory
    of 775 affected structures.
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
- href: https://data.humdata.org/dataset/unosat-deir-al-balah-comprehensive-damage-assessment-gaza-strip-21-october-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from armed conflict/hostilities
      in Deir Al-Balah
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
  description: Palestine - UNOSAT Deir Al-Balah Comprehensive Damage Assessment -
    Gaza Strip - 21 October 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3707/UNOSAT_CE20231007PSE_GDB_20231025.zip
  format: Geodatabase
  id: resource_5d7ee960
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20231007PSE_GDB_20231025.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pse_unosat_deiralbalahcomprehensived_20231025
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
  start: '2023-10-25'
temporal_resolution: null
title: Palestine - UNOSAT Deir Al-Balah Comprehensive Damage Assessment - Gaza Strip
  - 21 October 2023
version: null
vulnerability: null
---
