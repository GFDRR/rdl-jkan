---
attributions:
- entity:
    affiliation: null
    email: 'jrc-effis@ec.europa.eu '
    name: European Forest Fire Information System (EFFIS)
    url: https://forest-fire.emergency.copernicus.eu
  id: Entity_1
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: 'jrc-effis@ec.europa.eu '
  name: JRC EFFIS Team
  url: https://forest-fire.emergency.copernicus.eu
creator:
  affiliation: null
  email: 'jrc-effis@ec.europa.eu '
  name: European Forest Fire Information System (EFFIS)
  url: https://forest-fire.emergency.copernicus.eu
dataset_id: rdls_hzd-jrc_drmkc_wildfires
description: Deterministic wildfires hazard
details: Harmonized wildfire risk assessment for the pan-European region through the
  EFFIS system, integrating fire danger (hazard) and vulnerability components across
  people, ecological, and economic values. This prototype methodology provides consistent
  continental-scale risk rankings and spatial data layers to support EU regulatory
  compliance, inform fire management strategies, and establish a baseline for comprehensive
  wildfire risk evaluation across Member States and the broader European region.
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 5
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFFIS_Wildfires_Hazard
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: low_risk
      occurrence:
        deterministic:
          description: null
          index_criteria: Low risk (EFFIS wildfire danger class)
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFFIS_Wildfires_Hazard
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: intermediate_risk
      occurrence:
        deterministic:
          description: null
          index_criteria: Intermediate risk (EFFIS wildfire danger class)
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFFIS_Wildfires_Hazard
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: high_risk
      occurrence:
        deterministic:
          description: null
          index_criteria: High risk (EFFIS wildfire danger class)
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFFIS_Wildfires_Hazard
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: danger_by_weather
      occurrence:
        deterministic:
          description: null
          index_criteria: Danger by weather (EFFIS wildfire danger class)
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFFIS_Wildfires_Hazard
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: danger_by_thermalanomalies
      occurrence:
        deterministic:
          description: null
          index_criteria: Danger by thermalanomalies (EFFIS wildfire danger class)
          thresholds: null
        empirical: null
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: EFFIS_Wildfires_Hazard
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: Wildfires_Hazard
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: European Forest Fire Information System (EFFIS)
    risk_data_type: null
    type: model
    url: https://forest-fire.emergency.copernicus.eu
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: European Forest Fire Information System (EFFIS)
  url: https://forest-fire.emergency.copernicus.eu/about-effis/
publisher:
  affiliation: null
  email: jrc-effis@ec.europa.eu
  name: European Forest Fire Information System (EFFIS)
  url: https://forest-fire.emergency.copernicus.eu/about-effis/
purpose: To assess wildfire risk across the pan-European region by evaluating fire
  danger and vulnerability to support fire management strategies and EU policy compliance.
referenced_by:
- author_names:
  - "Jes\xFAs San-Miguel-Ayanz"
  - Ernst Schulte
  - Guido Schmuck
  - Andrea Camia
  - Peter Strobl
  - Giorgio Liberta
  - Cristiano Giovando
  - Roberto Boca
  - Fernando Sedano
  - Pieter Kempeneers
  - Daniel McInerney
  - Ceri Withmore
  - Sandra Santos de Oliveira
  - Marcos Rodrigues
  - Tracy Durrant
  - Paolo Corti
  - Friderike Oehler
  - Lara Vilar
  - Giuseppe Amatulli
  date_published: '2012-03-14'
  doi: http://dx.doi.org/10.5772/28441
  id: Ref_1
  name: 'Comprehensive Monitoring of Wildfires in Europe: The European Forest Fire
    Information System (EFFIS)'
  url: https://www.intechopen.com/chapters/31818
resources:
- access_url: https://forest-fire.emergency.copernicus.eu/apps/fire.risk.viewer/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3035
  description: 'Aggregated wildfire risk index: prevalence of the lower-risk class
    in the spatial cell (percentage), modelling wildfires and considering any other
    typology of vegetation fires only for the potential risk to become a wildfire
    [preliminary prototype approximation]. The maximum extent of possible values ranges
    from 0 to 1 (100 %), continuous values, so that the data satisfy the array-based
    semantic constraint ::proportion:: (semantic array programming). In each spatial
    cell c, the variable is expressed as prevalence in the cell area (%).'
  download_url: https://gwis-reports.s3-eu-west-1.amazonaws.com/WFRA/var-risk-aggr-l3p122_unit-dimensionless_stat-rank_class3-1.zip
  format: null
  id: low_risk
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 12500
  temporal: null
  temporal_resolution: null
  title: Low risk (aggr.  wildfire risk) in the European Wildfire Risk Assessment
- access_url: https://forest-fire.emergency.copernicus.eu/apps/fire.risk.viewer/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3035
  description: 'Aggregated wildfire risk index: prevalence of the intermediate-risk
    class in the spatial cell (percentage), modelling wildfires and considering any
    other typology of vegetation fires only for the potential risk to become a wildfire
    [preliminary prototype approximation]. The maximum extent of possible values ranges
    from 0 to 1 (100 %), continuous values, so that the data satisfy the array-based
    semantic constraint ::proportion:: (semantic array programming). In each spatial
    cell c, the variable is expressed as prevalence in the cell area (%).'
  download_url: https://gwis-reports.s3-eu-west-1.amazonaws.com/WFRA/var-risk-aggr-l3p122_unit-dimensionless_stat-rank_class3-2.zip
  format: null
  id: intermediate_risk
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 12500
  temporal: null
  temporal_resolution: null
  title: Intermediate risk (aggr.  wildfire risk) in the European Wildfire Risk Assessment
- access_url: https://forest-fire.emergency.copernicus.eu/apps/fire.risk.viewer/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3035
  description: 'Aggregated wildfire risk index: prevalence of the higher-risk class
    in the spatial cell (percentage), modelling wildfires and considering any other
    typology of vegetation fires only for the potential risk to become a wildfire
    [preliminary prototype approximation]. The maximum extent of possible values ranges
    from 0 to 1 (100 %), continuous values, so that the data satisfy the array-based
    semantic constraint ::proportion:: (semantic array programming). In each spatial
    cell c, the variable is expressed as prevalence in the cell area (%).'
  download_url: https://gwis-reports.s3-eu-west-1.amazonaws.com/WFRA/var-risk-aggr-l3p122_unit-dimensionless_stat-rank_class3-3.zip
  format: null
  id: high_risk
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 12500
  temporal: null
  temporal_resolution: null
  title: High risk (aggr.  wildfire risk) in the European Wildfire Risk Assessment
- access_url: https://forest-fire.emergency.copernicus.eu/apps/fire.risk.viewer/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3035
  description: "Days with high-to-extreme fire danger by weather (FWI \u2265 30) -\
    \ uncertainty aggregation of the model\u2019s runs: median value [preliminary\
    \ prototype approximation]. The maximum extent of possible values ranges from\
    \ 0 to 1 (100 %), continuous values, so that the data satisfy the array-based\
    \ semantic constraint ::proportion:: (semantic array programming). In each spatial\
    \ cell c, the variable is expressed as percentile (%), i.e. as percentage of the\
    \ other cells whose value is less than in c."
  download_url: https://gwis-reports.s3-eu-west-1.amazonaws.com/WFRA/var-danger-FWI30_unit-dimensionless.zip
  format: null
  id: danger_by_weather
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 12500
  temporal: null
  temporal_resolution: null
  title: Danger by weather (FWI30-days) in the European Wildfire Risk Assessment
- access_url: https://forest-fire.emergency.copernicus.eu/apps/fire.risk.viewer/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3035
  description: "Wildfire danger by observed frequency of thermal anomalies (MODIS/VIIRS),\
    \ with thermal anomalies ranked against their expected association with wildfires\
    \ (lower ranking for other vegetation fires) - uncertainty aggregation of the\
    \ model\u2019s runs: median value [preliminary prototype approximation]. The maximum\
    \ extent of possible values ranges from 0 to 1 (100 %), continuous values, so\
    \ that the data satisfy the array-based semantic constraint ::proportion:: (semantic\
    \ array programming). In each spatial cell c, the variable is expressed as percentile\
    \ (%), i.e. as percentage of the other cells whose value is less than in c."
  download_url: https://gwis-reports.s3-eu-west-1.amazonaws.com/WFRA/var-danger-TA_unit-dimensionless.zip
  format: null
  id: danger_by_thermalanomalies
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 12500
  temporal: null
  temporal_resolution: null
  title: Danger by wildfire thermal anomalies in the European Wildfire Risk Assessment
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-jrc_drmkc_wildfires
spatial:
  bbox: null
  centroid: null
  countries:
  - AUT
  - BEL
  - BGR
  - HRV
  - CYP
  - CZE
  - DNK
  - EST
  - FIN
  - FRA
  - DEU
  - GRC
  - HUN
  - IRL
  - ITA
  - LVA
  - LTU
  - LUX
  - MLT
  - NLD
  - POL
  - PRT
  - ROU
  - SVK
  - SVN
  - ESP
  - SWE
  gazetteer_entries:
  - description: Europe
    id: Location_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6255148/europe.html
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: EFFIS Wildfires Hazard Map
version: '1'
vulnerability: null
---
