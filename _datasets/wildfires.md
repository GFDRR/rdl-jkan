---
contact_point:
  email: 'jrc-effis@ec.europa.eu '
  name: JRC EFFIS Team
  url: https://forest-fire.emergency.copernicus.eu
creator:
  email: 'jrc-effis@ec.europa.eu '
  name: European Forest Fire Information System (EFFIS)
  url: https://forest-fire.emergency.copernicus.eu
dataset_id: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/atlas/metadata/wildfire_effis
description: Deterministic wildfires hazard
details: Harmonized wildfire risk assessment for the pan-European region through the
  EFFIS system, integrating fire danger (hazard) and vulnerability components across
  people, ecological, and economic values. This prototype methodology provides consistent
  continental-scale risk rankings and spatial data layers to support EU regulatory
  compliance, inform fire management strategies, and establish a baseline for comprehensive
  wildfire risk evaluation across Member States and the broader European region.
exposure: null
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: empirical
  hazard_type: wildfire
  intensity: ''
  occurrence_range: ''
  processes: wildfire
license: CC-BY-4.0
loss: null
project: European Forest Fire Information System (EFFIS)
publisher:
  email: jrc-effis@ec.europa.eu
  name: European Forest Fire Information System (EFFIS)
  url: https://forest-fire.emergency.copernicus.eu/about-effis/
purpose: To assess wildfire risk across the pan-European region by evaluating fire
  danger and vulnerability to support fire management strategies and EU policy compliance.
resources:
- coordinate_system: EPSG:3035
  description: 'Aggregated wildfire risk index: prevalence of the lower-risk class
    in the spatial cell (percentage), modelling wildfires and considering any other
    typology of vegetation fires only for the potential risk to become a wildfire
    [preliminary prototype approximation]. The maximum extent of possible values ranges
    from 0 to 1 (100 %), continuous values, so that the data satisfy the array-based
    semantic constraint ::proportion:: (semantic array programming). In each spatial
    cell c, the variable is expressed as prevalence in the cell area (%).'
  download_url: https://gwis-reports.s3-eu-west-1.amazonaws.com/WFRA/var-risk-aggr-l3p122_unit-dimensionless_stat-rank_class3-1.zip
  format: geotiff
  id: low_risk
  spatial_resolution: 12500
  title: Low risk (aggr.  wildfire risk) in the European Wildfire Risk Assessment
- coordinate_system: EPSG:3035
  description: 'Aggregated wildfire risk index: prevalence of the intermediate-risk
    class in the spatial cell (percentage), modelling wildfires and considering any
    other typology of vegetation fires only for the potential risk to become a wildfire
    [preliminary prototype approximation]. The maximum extent of possible values ranges
    from 0 to 1 (100 %), continuous values, so that the data satisfy the array-based
    semantic constraint ::proportion:: (semantic array programming). In each spatial
    cell c, the variable is expressed as prevalence in the cell area (%).'
  download_url: https://gwis-reports.s3-eu-west-1.amazonaws.com/WFRA/var-risk-aggr-l3p122_unit-dimensionless_stat-rank_class3-2.zip
  format: geotiff
  id: intermediate_risk
  spatial_resolution: 12500
  title: Intermediate risk (aggr.  wildfire risk) in the European Wildfire Risk Assessment
- coordinate_system: EPSG:3035
  description: 'Aggregated wildfire risk index: prevalence of the higher-risk class
    in the spatial cell (percentage), modelling wildfires and considering any other
    typology of vegetation fires only for the potential risk to become a wildfire
    [preliminary prototype approximation]. The maximum extent of possible values ranges
    from 0 to 1 (100 %), continuous values, so that the data satisfy the array-based
    semantic constraint ::proportion:: (semantic array programming). In each spatial
    cell c, the variable is expressed as prevalence in the cell area (%).'
  download_url: https://gwis-reports.s3-eu-west-1.amazonaws.com/WFRA/var-risk-aggr-l3p122_unit-dimensionless_stat-rank_class3-3.zip
  format: geotiff
  id: high_risk
  spatial_resolution: 12500
  title: High risk (aggr.  wildfire risk) in the European Wildfire Risk Assessment
- coordinate_system: EPSG:3035
  description: "Days with high-to-extreme fire danger by weather (FWI \u2265 30) -\
    \ uncertainty aggregation of the model\u2019s runs: median value [preliminary\
    \ prototype approximation]. The maximum extent of possible values ranges from\
    \ 0 to 1 (100 %), continuous values, so that the data satisfy the array-based\
    \ semantic constraint ::proportion:: (semantic array programming). In each spatial\
    \ cell c, the variable is expressed as percentile (%), i.e. as percentage of the\
    \ other cells whose value is less than in c."
  download_url: https://gwis-reports.s3-eu-west-1.amazonaws.com/WFRA/var-danger-FWI30_unit-dimensionless.zip
  format: geotiff
  id: danger_by_weather
  spatial_resolution: 12500
  title: Danger by weather (FWI30-days) in the European Wildfire Risk Assessment
- coordinate_system: EPSG:3035
  description: "Wildfire danger by observed frequency of thermal anomalies (MODIS/VIIRS),\
    \ with thermal anomalies ranked against their expected association with wildfires\
    \ (lower ranking for other vegetation fires) - uncertainty aggregation of the\
    \ model\u2019s runs: median value [preliminary prototype approximation]. The maximum\
    \ extent of possible values ranges from 0 to 1 (100 %), continuous values, so\
    \ that the data satisfy the array-based semantic constraint ::proportion:: (semantic\
    \ array programming). In each spatial cell c, the variable is expressed as percentile\
    \ (%), i.e. as percentage of the other cells whose value is less than in c."
  download_url: https://gwis-reports.s3-eu-west-1.amazonaws.com/WFRA/var-danger-TA_unit-dimensionless.zip
  format: geotiff
  id: danger_by_thermalanomalies
  spatial_resolution: 12500
  title: Danger by wildfire thermal anomalies in the European Wildfire Risk Assessment
risk_data_type:
- hazard
schema: rdl-02
slug: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/atlas/metadata/wildfire_effis
spatial:
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
title: Wildfires
version: '1'
vulnerability: null
---
