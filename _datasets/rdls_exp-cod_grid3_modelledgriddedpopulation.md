---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop Research Group
    url: https://data.humdata.org/dataset/modelled-gridded-population-estimates-for-cod-2018-v2
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development)
    url: https://data.humdata.org/dataset/modelled-gridded-population-estimates-for-cod-2018-v2
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/modelled-gridded-population-estimates-for-cod-2018-v2
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/modelled-gridded-population-estimates-for-cod-2018-v2
dataset_id: rdls_exp-cod_grid3_modelledgriddedpopulation
description: 'These data were produced by the WorldPop Research Group at the University
  of Southampton. This work is part of the GRID3 (Geo-Referenced Infrastructure and
  Demographic Data for Development) project funded by the Bill and Melinda Gates Foundation
  (BMGF) and the United Kingdom Foreign, Commonwealth & Development Office (OPP1182425).
  Project partners include WorldPop at the University of Southampton, the United Nations
  Population Fund ( UNFPA ), Center for International Earth Science Information Network
  ( CIESIN ) in the Earth Institute at Columbia University, and the Flowminder Foundation.
  The modelling work was led by Gianluca Boo and Edith Darin with the support from
  Douglas R. Leasure and Claire A. Dooley. Coordination was provided by Heather R.
  Chamberlain and oversight by Andrew J. Tatem and Attila N. Lazar. The support of
  the whole WorldPop Research Group is acknowledged. The UCLA-DRC Health Research
  and Training Program, the Kinshasa School of Public Health (KSPH), and the Bureau
  Central du Recensement (BCR) coordinated and conducted the two microcensus rounds.
  The Oak Ridge National Laboratory contributed to the first round of microcensus.
  We acknowledge the contribution of the many individuals within these institutions.
  Recommended citation: Boo G, Darin E, Leasure DR, Dooley CA, Chamberlain HR, Lazar
  AN, Tatem AJ. 2020. Modelled gridded population estimates for the Kinshasa, Kongo-Central,
  Kwango, Kwilu, and Mai-Ndombe provinces in the Democratic Republic of the Congo,
  version 2.0. WorldPop, University of Southampton. doi:10.5258/SOTON/WP00669. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/modelled-gridded-population-estimates-for-cod-2018-v2]'
details: __Recommended citation:__ _Boo G, Darin E, Leasure DR, Dooley CA, Chamberlain
  HR, Lazar AN, Tatem AJ. 2020. Modelled gridded population estimates for the Kinshasa,
  Kongo-Central, Kwango, Kwilu, and Mai-Ndombe provinces in the Democratic Republic
  of the Congo, version 2.0. WorldPop, University of Southampton. doi:10.5258/SOTON/WP00669_
  For further details, please, read COD_population_v2_0_README.pdf Contact release@worldpop.org
  for more information.
exposure:
- asset_type:
    description: Gridded population estimates by age and sex for five provinces in
      Democratic Republic of the Congo
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
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Gridded population estimates were produced by WorldPop using census
    data integrated with satellite imagery and spatial modeling techniques to generate
    high-resolution population density grids at approximately 100m resolution. The
    dataset was developed as part of the GRID3 project to provide geo-referenced demographic
    data for development and disaster risk assessment in five provinces of the Democratic
    Republic of the Congo.
  sources:
  - id: source_1
    license: null
    name: WorldPop Research Group
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/modelled-gridded-population-estimates-for-cod-2018-v2
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bottom-up gridded population estimates (100m) for Democratic Republic
    of the Congo. This zip file contains a geotiff raster with estimates of total
    population size for each approximately 100 m grid cell across the study area.
    It also contains a geotiff raster with estimates of uncertainty in the population
    estimates.
  download_url: https://wopr.worldpop.org/download/113
  format: null
  id: resource_1ef048d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COD_population_v2_0_gridded.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bottom-up gridded population estimates (~100m) for specific age-sex
    groups. This zip file contains geotiff rasters with estimates of population sizes
    for individual age-sex groups for each approximately 100 m grid cell across the
    study area.
  download_url: https://wopr.worldpop.org/download/120
  format: null
  id: resource_14bff7cf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COD_population_v2_0_agesex.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mastergrid for gridded population estimates. This geotiff raster contains
    the mastergrid used to define where population estimates were made. It contains
    a value of 1 where population estimates were made and a value of 0 or NA everywhere
    else. Cell IDs from the mastergrid can be used to lookup values in the SQL database.
  download_url: https://wopr.worldpop.org/download/117
  format: null
  id: resource_2e148d79
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COD_population_v2_0_mastergrid.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'README: COD Population v2.0. This README file provides information
    about the data included in the data release, how it was produced, source data
    that were used, and known assumptions and limitations of the results.'
  download_url: https://wopr.worldpop.org/download/114
  format: null
  id: resource_a7d68735
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COD_population_v2_0_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: SQL database with Bayesian posterior population predictions. This SQLite
    database contains samples from the Bayesian posterior predictions of population
    size in each grid cell. The database can be used to develop applications that
    query the population estimates
  download_url: https://wopr.worldpop.org/download/115
  format: SQL
  id: resource_427c1736
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COD_population_v2_0_sql.sql
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Image tiles for gridded population estimates. These image tiles (XYZ
    format) allow for rapid display of the 100 m gridded population estimates across
    the study area in web applications.
  download_url: https://wopr.worldpop.org/download/116
  format: PNG
  id: resource_f3e6ec8d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COD_population_v2_0_tiles.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cod_grid3_modelledgriddedpopulation
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Modelled gridded population estimates for the Kinshasa, Kongo-Central, Kwango,
  Kwilu, and Mai-Ndombe provinces in the Democratic Republic of the Congo 2018, version
  2.0
version: null
vulnerability: null
---
