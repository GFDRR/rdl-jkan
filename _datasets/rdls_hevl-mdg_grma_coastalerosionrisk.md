---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: alvaro.prida@axaclimate.com
  name: Alvaro Prida
  url: null
creator:
  affiliation: null
  email: null
  name: AXA Climate
  url: https://climate.axa
dataset_id: rdls_hevl-mdg_grma_coastalerosionrisk
description: Comprehensive coastal erosion risk assessment for Madagascar, integrating
  hazard polygons delineating projected erosion extents, economic loss estimates (GDP),
  and population displacement impacts at the commune level (ADM3). The assessment
  covers future time horizons (2050 and 2085) under socioeconomic pathways SSP2 and
  SSP5, combining coastal erosion projections with spatially distributed economic
  and demographic exposure data and binary impact modelling.
details: 'This dataset merges three components of Madagascar''s coastal erosion risk
  profile. Hazard: Erosion footprints derived from post-processing of LISCOAST projections
  (Vousdoukas et al., 2019), accounting for ambient coastline dynamics, shoreline
  retreat due to sea-level rise, and storm-induced erosion (RP100). Erosion distances
  along coastal transects (~500 m spacing) were interpolated and combined with the
  baseline shoreline (OSM 2020) to generate polygons. Economic exposure: Spatial GDP
  distribution from LitPop (2020) for baseline and Wang et al. (2023) SSP-based 1
  km gridded GDP projections for future scenarios. Population exposure: WorldPop (2020)
  gridded population at 100 m resolution, validated against INSTAT administrative
  counts, with Wang et al. (2022) SSP-based 1 km population projections for future
  scenarios. Vulnerability: Binary impact model whereby all assets and population
  within projected erosion extents are considered fully affected.'
exposure:
- asset_type: null
  category: economic_indicator
  id: exposure_economic_001
  metrics:
  - dimension: product
    id: metric_gdp
    measurement:
      quantity_kind: currency
      unit: USD
- asset_type: null
  category: population
  id: exposure_population_001
  metrics:
  - dimension: population
    id: metric_pop
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: deterministic
      calculation_method: null
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_ce_001
        intensity_measure: AA:km2
        process: coastal_flood
        trigger:
          process: coastal_flood
          type: flood
        type: flood
      id: event_set_ce_001
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: source_ce_liscoast
    license: https://creativecommons.org/licenses/by/4.0/
    name: Global shoreline change projections from LISCOAST
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.4121/uuid:82c1dc0d-5485-43d8-901a-ce7f26cda35d
    used_in: hazard
  - id: source_ce_litpop_gdp
    license: https://creativecommons.org/licenses/by/4.0/
    name: LitPop GDP (2020)
    risk_data_type: null
    type: dataset
    url: https://climada-python.readthedocs.io/en/stable/user-guide/climada_entity_LitPop.html
    used_in: exposure
  - id: source_ce_projected_gdp
    license: https://creativecommons.org/licenses/by/4.0/
    name: "Projected 1 km GDP distributions (2020\u20132100) under SSPs"
    risk_data_type: null
    type: dataset
    url: https://zenodo.org/records/7898409
    used_in: exposure
  - id: source_ce_worldpop
    license: https://creativecommons.org/licenses/by/4.0/
    name: WorldPop Population (2020)
    risk_data_type: null
    type: dataset
    url: https://hub.worldpop.org/geodata/summary?id=49697
    used_in: exposure
  - id: source_ce_instat
    license: https://creativecommons.org/licenses/by/4.0/
    name: INSTAT Population (Madagascar)
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
  - id: source_ce_projected_pop
    license: https://creativecommons.org/licenses/by/4.0/
    name: "Projected 1 km population distributions (2020\u20132100) under SSPs"
    risk_data_type: null
    type: dataset
    url: https://figshare.com/articles/dataset/Projecting_1_km-grid_population_distributions_from_2020_to_2100_globally_under_shared_socioeconomic_pathways/19608594
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: product
    description: Total GDP lost within projected erosion extents per commune
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_ce_economic
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: gross
  - asset_category: population
    asset_dimension: population
    description: Population displaced due to coastal erosion per commune
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_ce_population
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: count
project:
  name: GRMA Madagascar - Phase 1
  url: https://www.resiliencemada.gov.mg
publisher:
  affiliation: null
  email: null
  name: Global Risk Modelling Alliance
  url: https://grma.global
purpose: This dataset was developed during the first phase of GRMA's project in Madagascar.
  This project aimed at updating Madagascar's risk profile and assessing risk evolution
  under climate change.
referenced_by:
- author_names:
  - Vousdoukas, M., Ranasinghe, R., Mentaschi, L., Plomaritis, T., Athanasiou, P.,
    Luijendijk, A. and Feyen, L.
  date_published: '2020-03-02'
  doi: https://doi.org/10.1038/s41558-020-0697-0
  id: reference_ce_vousdoukas
  name: Sandy coastlines under threat of erosion
  url: https://www.nature.com/articles/s41558-020-0697-0
- author_names:
  - AXA Climate
  date_published: null
  doi: null
  id: reference_ce_grma_report
  name: "Rapport m\xE9thodologique (GRMA) - English version"
  url: https://www.resiliencemada.gov.mg/catalogue/#/document/1290
- author_names:
  - Eberenz, S., et al.
  date_published: null
  doi: null
  id: reference_ce_litpop
  name: 'LitPop GDP: High-Resolution Gridded GDP Based on Lights and Population'
  url: https://climada-python.readthedocs.io/en/stable/user-guide/climada_entity_LitPop.html
- author_names:
  - Wang, T., Sun, F.
  date_published: '2022-10-07'
  doi: https://doi.org/10.1038/s41597-022-01300-x
  id: reference_ce_wang_gdp
  name: Projecting 1 km-grid GDP distributions from 2020 to 2100 under Shared Socioeconomic
    Pathways
  url: https://www.nature.com/articles/s41597-022-01300-x
- author_names:
  - WorldPop Project
  date_published: null
  doi: null
  id: reference_ce_worldpop
  name: WorldPop Population Count Dataset, Madagascar 2020
  url: https://hub.worldpop.org/geodata/summary?id=49697
- author_names:
  - Wang, T., Sun, F.
  date_published: '2022-04-20'
  doi: https://doi.org/10.1038/s41597-022-01675-x
  id: reference_ce_wang_pop
  name: Projecting 1 km-grid population distributions from 2020 to 2100 globally under
    shared socioeconomic pathways
  url: https://www.nature.com/articles/s41597-022-01675-x
resources:
- access_url: https://www.resiliencemada.gov.mg/catalogue/uuid/5d02d6ab-a914-4842-ac5c-349b14e0c7a9
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Polygons delineating projected coastal areas expected to undergo erosion
    under future time horizons (2050 and 2085) and socioeconomic pathways (SSP2 and
    SSP5), derived from LISCOAST projections.
  download_url: null
  format: null
  id: resource_ce_hazard_polygons
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Coastal Erosion - Hazard Polygons
- access_url: https://www.resiliencemada.gov.mg/catalogue/uuid/5d02d6ab-a914-4842-ac5c-349b14e0c7a9
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Aggregated economic loss (GDP) due to projected coastal erosion at
    the commune level (ADM3) in Madagascar, for different time horizons and socioeconomic
    pathways.
  download_url: null
  format: null
  id: resource_ce_economic_risk
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Commune level (administrative level 3, ADM3)
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Coastal Erosion - Economic Risk per Commune
- access_url: https://www.resiliencemada.gov.mg/catalogue/uuid/5d02d6ab-a914-4842-ac5c-349b14e0c7a9
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Aggregated affected population due to projected coastal erosion at
    the commune level (ADM3) in Madagascar, for different time horizons and socioeconomic
    pathways.
  download_url: null
  format: null
  id: resource_ce_population_risk
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Commune level (administrative level 3, ADM3)
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Coastal Erosion - Population Impacts per Commune
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-mdg_grma_coastalerosionrisk
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Coastal Erosion Risk Assessment for Madagascar
version: '1.0'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility: []
    socio_economic: []
    vulnerability:
    - analysis_details: null
      approach: empirical
      category: economic_indicator
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: hazard_flood
        intensity_measure: AA:km2
        process: coastal_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: vuln_ce_economic
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      relationship: discrete
      taxonomy: null
    - analysis_details: 'Binary vulnerability: all population in eroded areas considered
        displaced'
      approach: empirical
      category: population
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: vuln_ce_population
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: inferred
        type: direct
      relationship: discrete
      taxonomy: null
---
