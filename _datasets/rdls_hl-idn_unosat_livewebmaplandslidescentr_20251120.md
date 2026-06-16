---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-landslides-in-central-java-indonesia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-landslides-in-central-java-indonesia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-landslides-in-central-java-indonesia
dataset_id: rdls_hl-idn_unosat_livewebmaplandslidescentr_20251120
description: 'UNOSAT code: LS20251118IDN This application provides flood impact assessments
  related to Landslide in Java, Indonesia- November 2025. Important note: The boundaries
  and names shown, and the designations used on this map, do not imply official endorsement
  or acceptance by the United Nations. The designations employed and the presentation
  of material on this map do not imply the expression of any opinion whatsoever on
  the part of the Secretariat of the United Nations concerning the legal status of
  any country, territory, city or area or of its authorities, or concerning the delimitation
  of its frontiers or boundaries.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-landslides-in-central-java-indonesia]'
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
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery to detect notable
    changes and assess landslide impacts in Central Java. The analysis employed visual
    interpretation of multi-temporal satellite data to identify affected areas and
    generate impact assessments for the November 2025 landslide event.
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
- href: https://data.humdata.org/dataset/unosat-live-web-map-landslides-in-central-java-indonesia
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct impact assessment of landslide event on affected areas in
      Central Java
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: UNOSAT Live web map - Landslides in Central Java, Indonesia (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4219/LS20251118IDN_gdb.zip
  format: Geodatabase
  id: resource_07597fb9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20251118IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live web map - Landslides in Central Java, Indonesia (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4219/LS20251118IDN_gdb.zip
  format: null
  id: resource_2ffbe4ec
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20251118IDN_gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-idn_unosat_livewebmaplandslidescentr_20251120
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-11-20'
temporal_resolution: null
title: UNOSAT Live web map - Landslides in Central Java, Indonesia
version: null
vulnerability: null
---
