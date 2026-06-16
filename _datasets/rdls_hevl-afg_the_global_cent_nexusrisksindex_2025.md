---
attributions:
- entity:
    affiliation: null
    email: null
    name: IPCC
    url: https://data.humdata.org/dataset/afghanistan-nexus-risks-index
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM Risk Index
    url: https://data.humdata.org/dataset/afghanistan-nexus-risks-index
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ERA5
    url: https://data.humdata.org/dataset/afghanistan-nexus-risks-index
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GPCC
    url: https://data.humdata.org/dataset/afghanistan-nexus-risks-index
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GRACE
    url: https://data.humdata.org/dataset/afghanistan-nexus-risks-index
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WGMS
    url: https://data.humdata.org/dataset/afghanistan-nexus-risks-index
  id: attribution_6
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WMO Global Indicators
    url: https://data.humdata.org/dataset/afghanistan-nexus-risks-index
  id: attribution_7
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Global Centre for Risk and Innovation (GCRI)
  url: https://data.humdata.org/dataset/afghanistan-nexus-risks-index
creator:
  affiliation: null
  email: null
  name: The Global Centre for Risk and Innovation (GCRI)
  url: https://data.humdata.org/dataset/afghanistan-nexus-risks-index
dataset_id: rdls_hevl-afg_the_global_cent_nexusrisksindex_2025
description: "Overview This dataset provides a technically validated, multi-sectoral\
  \ and system-wide Nexus Risk Index for Afghanistan. It contains 100 curated indicators\
  \ (IND001-IND100), tailored to fragile and conflict-affected settings, covering\
  \ climate, health, energy, infrastructure, food, water, security, governance, and\
  \ environmental systems. Methodological Foundations IPBES Nexus Assessment (2024)\
  \ : Used as the core methodological framework Data Sources : IPCC, INFORM Risk Index,\
  \ WMO Global Indicators, GRACE, WGMS, ERA5, GPCC, OSI SAF, and more Processing :\
  \ Standardized, rebaselined, and interpolated using climate-model aligned adjustments,\
  \ temporal smoothing, and system simulations Validation : Expert-reviewed under\
  \ the GCRI Nexus Ecosystem as part of the Nexus Reports quarterly cycle Structure\
  \ Each indicator includes: - Disaster Risk Intelligence (DRI) : Specialized interpretation\
  \ of system risk, derived from climate models, hazard projections, or sector disruption\
  \ patterns - Disaster Risk Financing (DRF) : Tailored financial exposure, shock-buffering\
  \ capacity, and anticipatory resource needs - Disaster Risk Reduction (DRR) : Mitigation\
  \ and adaptation strategy options, aligned with Afghanistan's capacities and SDGs\
  \ License and Restrictions \u201A\xF6\u2020\xD4\u220F\xE8 This dataset is not intended\
  \ for sensitive or life-critical operations. It is configured specifically for Nexus-based\
  \ scenario modeling and anticipatory governance applications. Adaptability to external\
  \ tools and platforms requires expert interpretation. Technical Documentation File\
  \ formats: .csv , .txt , .md Metadata compliant with HDX and GitHub standards For\
  \ full documentation, visit: https://therisk.global Contact For support or inquiries:\
  \ \uF8FF\xFC\xEC\xDF contact@therisk.global \uF8FF\xFC\xE5\xEA https://therisk.global.\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-nexus-risks-index]"
details: "\u201A\xF6\u2020 Data Considerations and Limitations Data Quality Variance:\
  \ Data quality and resolution vary across sources. Some indicators rely on interpolated\
  \ or modeled data where direct observation is unavailable-particularly in conflict-affected\
  \ or remote regions of Afghanistan. Missing and Estimated Data: Regions inaccessible\
  \ due to insecurity or lacking monitoring infrastructure may contain estimated or\
  \ proxy-derived values. This includes humanitarian needs, infrastructure damage,\
  \ and local governance indicators. Temporal Disparities: Some datasets are historical\
  \ (e.g., temperature since 1850), while others are near-real-time or updated annually.\
  \ Users should consult indicator metadata for update frequency and source details.\
  \ Derived and Composite Metrics: Several indicators are aggregates of multiple sub-indicators\
  \ or derived through composite modeling, which may introduce bias or error propagation\
  \ depending on methodological assumptions. Context-Specific Interpretation: The\
  \ Nexus Risk Index is tailored for the Afghanistan context but can be adapted elsewhere.\
  \ However, interpretations must account for the country-specific political economy,\
  \ cultural dynamics, and environmental thresholds. Use Restrictions: The dataset\
  \ is designed for research, humanitarian coordination, and resilience planning.\
  \ It is not suitable for commercial or high-stakes operational decision-making without\
  \ independent validation. Users must not use this data for predictive policing,\
  \ insurance risk calculations, or financial investment analysis without consultation\
  \ with experts."
exposure:
- asset_type:
    description: Population exposure sensitivity captured through Exposure_Sensitivity_Index
      across multiple nexus dimensions
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: index
      unit: null
- asset_type:
    description: Infrastructure and energy system exposure indicators
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: index
      unit: null
- asset_type:
    description: Food and water system exposure indicators
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_3
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: index
      unit: null
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC0-1.0
lineage:
  description: The Nexus Risk Index integrates 100 curated indicators from over 30
    data sources using the IPBES Nexus Assessment framework methodology. High-resolution
    modeling evaluates systemic risks across climate, health, energy, infrastructure,
    food, water, security, governance, and environmental systems. Indicators are normalized,
    scored for risk probability and impact severity, and aggregated into composite
    nexus risk scores.
  sources:
  - id: source_1
    license: null
    name: IPCC
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: INFORM Risk Index
    risk_data_type:
    - vulnerability
    type: model
    url: null
    used_in: vulnerability
  - id: source_3
    license: null
    name: ERA5
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: GPCC
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: GRACE
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_6
    license: null
    name: WGMS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_7
    license: null
    name: WMO Global Indicators
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-nexus-risks-index
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Composite risk scores and impact severity indices for climate and
      environmental hazards affecting population systems
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Infrastructure risk and resilience gap metrics linked to disaster
      risk
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: damage
        modelling: observed
        type: total
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
  description: Afghanistan - Nexus Risks Index (Multi-sectoral and system-wide Nexus
    Risk Index for Afghanistan.)
  download_url: https://data.humdata.org/dataset/017e288e-57ef-46dd-ba90-fccc3a4b447f/resource/18455b90-1592-478a-a3e8-6d8a30ddbd14/download/afghanistan_nexus_risk_index.csv
  format: null
  id: resource_18455b90
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afghanistan_Nexus_Risk_Index.csv
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-afg_the_global_cent_nexusrisksindex_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-03-31'
  start: '2025-01-01'
temporal_resolution: null
title: Afghanistan - Nexus Risks Index
version: null
vulnerability: null
---
