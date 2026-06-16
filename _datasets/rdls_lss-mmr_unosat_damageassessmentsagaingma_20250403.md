---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-sagaing-and-mandalay-myanmar-as-of-30-march-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-sagaing-and-mandalay-myanmar-as-of-30-march-2025
dataset_id: rdls_lss-mmr_unosat_damageassessmentsagaingma_20250403
description: "UNOSAT code: EQ20250328MMR, GDACS ID: 1474477 This map illustrates the\
  \ number of affected buildings within specific Towns/Village Tracts boundaries of\
  \ interest in Sagaing and Mandalay, Myanmar, as of 30 March 2025. Within the analyzed\
  \ area-52 Towns/Village Tracts covering approximately 340 km\xC2\xB2, UNOSAT identified\
  \ 1,095 damaged structures and 1,325 potentially damaged ones. The analysis represents\
  \ areas where more than 50% of each Village Tract has been assessed for impact.\
  \ This is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-sagaing-and-mandalay-myanmar-as-of-30-march-2025]"
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
  description: UNOSAT analysts conducted post-event satellite imagery analysis comparing
    pre- and post-earthquake images to identify structural damage in 52 Towns/Village
    Tracts across Sagaing and Mandalay regions. Building damage was classified into
    confirmed damaged (1,095 structures) and potentially damaged (1,325 structures)
    categories, with analysis limited to areas where >50% of each Village Tract was
    assessed.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-sagaing-and-mandalay-myanmar-as-of-30-march-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from earthquake event EQ20250328MMR
      in Sagaing and Mandalay regions
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Damage Assessment in Sagaing and Mandalay, Myanmar as of 30 March 2025
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4096/EQ20250328MMR_gdb.zip
  format: Geodatabase
  id: resource_b1e2ed60
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20250328MMR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Sagaing and Mandalay, Myanmar as of 30 March 2025
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4096/EQ20250328MMR_SHP.zip
  format: null
  id: resource_4e1c7c05
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20250328MMR_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Sagaing and Mandalay, Myanmar as of 30 March 2025
    (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4096/DamageAssessment_EQ20250328MMR_Sagaing_MandalayRegions.xlsx
  format: null
  id: resource_bbf44b81
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DamageAssessment_EQ20250328MMR_Sagaing_MandalayRegions.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mmr_unosat_damageassessmentsagaingma_20250403
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
  start: '2025-04-03'
temporal_resolution: null
title: Damage Assessment in Sagaing and Mandalay, Myanmar as of 30 March 2025
version: null
vulnerability: null
---
