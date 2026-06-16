---
attributions:
- entity:
    affiliation: null
    email: null
    name: Mali Statistics Office Census Cartography Team
    url: https://data.humdata.org/dataset/census-cartography-based-gridded-population-estimates-for-mali-2020-version-1-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/census-cartography-based-gridded-population-estimates-for-mali-2020-version-1-0
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/census-cartography-based-gridded-population-estimates-for-mali-2020-version-1-0
dataset_id: rdls_exp-mli_worldpop_censuscartographybasedgri
description: "These data consist of modelled gridded population estimates produced\
  \ at a spatial resolution of approximately 100m across Mali. The estimates comprise\
  \ a combination of total population counts at enumeration area level collected by\
  \ the census cartography team of the Mali Statistics Office and modelled population\
  \ counts created using a Bayesian statistical model for areas that could not be\
  \ covered by the cartography team because of security issues. The main input data\
  \ for the model are the cartography data collected in the safe part of the country\
  \ in 2019-2020 (628 out of 714 Communes -administrative level 3-, that is 87% of\
  \ the country territory). Other essential input data include metrics derived from\
  \ building footprints, which were automatically delineated by Ecopia.AI in 2021\
  \ using satellite imagery collected by Maxar Technologies between 2010 and 2021.\
  \ The modelled population estimates represent the period of the census cartography,\
  \ but their consistency may be impacted by the accuracy of the building footprints.\
  \ These data were produced by the WorldPop Research Group at the University of Southampton\
  \ as part of the GRID3 Project, GRID3 (Geo-Referenced Infrastructure and Demographic\
  \ Data for Development) programme funded by the Bill and Melinda Gates Foundation\
  \ (BMGF) and the United Kingdom's Foreign, Commonwealth & Development Office (INV\
  \ 009579, formerly OPP 1182425). The study was approved by the Faculty Ethics Committee\
  \ of the University of Southampton (ERGO II 64957). The project was led by the Center\
  \ for International Earth Science Information Network (CIESIN) at Columbia University,\
  \ in collaboration with the WorldPop Research Group at the University of Southampton,\
  \ the United Nations Fund for Population (UNFPA) and the Malian Institut National\
  \ de la Statistique (INSTAT). The production of these data was led by Edith Darin\
  \ (WorldPop) with support from Matthias Ku\xE9pi\xE9 and Jean Wakam (UNFPA), Abdoul\
  \ Karim Diawara, Assa Gakou and Siaka Ciss\xE9 (Institut National de la Statistique),\
  \ and Attila N Lazar (WorldPop) and Andrew J Tatem (WorldPop). The authors acknowledge\
  \ the support of their respective institutions in the completion of this work. Recommended\
  \ citations WorldPop and Institut National de la Statistique du Mali. 2022. Census-cartography-based\
  \ gridded population estimates for Mali (2020), version 1.0. WorldPop, University\
  \ of Southampton. doi:10.5258/SOTON/WP00745 License These data may be redistributed\
  \ following the terms of a Creative Commons Share-Alike Attribution 4.0 International\
  \ (CC BY SA 4.0) license. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/census-cartography-based-gridded-population-estimates-for-mali-2020-version-1-0]"
details: null
exposure:
- asset_type:
    description: Gridded population estimates at 100m resolution derived from census
      cartography and Bayesian statistical modeling, including age-gender disaggregation
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Census population counts at enumeration area level from Mali Statistics
    Office (2019-2020) were combined with a Bayesian statistical model to produce
    gridded population estimates at 100m resolution across the entire country. The
    model was used to estimate populations in areas inaccessible to the cartography
    team due to security constraints, creating a complete national population surface
    with age-gender disaggregation.
  sources:
  - id: source_1
    license: null
    name: Mali Statistics Office Census Cartography Team
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/census-cartography-based-gridded-population-estimates-for-mali-2020-version-1-0
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
  description: This GeoTIFF raster represents estimates of total population counts
    within grid cells of approximately 100m across Mali The raster values are the
    mean of a posterior distribution (calibrated by the census cartography totals
    when available) and therefore include decimals (e.g. 0.5 people). An estimate
    of 0.5 people in two neighbouring cells indicates that one person lives somewhere
    within those two cells. NA values represent cells where no building footprint
    is present.
  download_url: https://wopr.worldpop.org/download/519
  format: null
  id: resource_15d00998
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLI_population_v1_0_gridded.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This binary GeoTIFF raster has a value of one if a grid cell of approximately
    100m contains at least one building footprint and zero if no building footprint
    is present. NA values indicate grid cells outside the boundaries of Mali.
  download_url: https://wopr.worldpop.org/download/520
  format: null
  id: resource_e609123a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLI_population_v1_0_mastergrid.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This README file provides information about the data included in the
    data release, how it was produced, source data that were used, and known assumptions
    and limitations of the results.
  download_url: https://wopr.worldpop.org/download/521
  format: null
  id: resource_bb6940b4
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLI_population_v1_0_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This SQLite database contains samples from the Bayesian posterior predictions
    of population size in each grid cell. The database can be used to develop applications
    that query the population estimates.
  download_url: https://wopr.worldpop.org/download/522
  format: SQL
  id: resource_27a5009a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLI_population_v1_0_sql.sql
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains geotiff rasters with estimates of population
    sizes for individual age-gender groups for each approximately 100 m grid cell
    across the study area.
  download_url: https://wopr.worldpop.org/download/523
  format: null
  id: resource_8c3c8761
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLI_population_v1_0_agegender.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mli_worldpop_censuscartographybasedgri
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Census-cartography-based gridded population estimates for Mali (2020), version
  1.0
version: null
vulnerability: null
---
